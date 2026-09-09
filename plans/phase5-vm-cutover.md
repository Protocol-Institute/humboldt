# Phase 5 implementation plan — VM cutover, service split, console access

**Status:** not started. Design of record: `redesign-2026-08.md` §12 and §12.2b.
**Target VM:** `humboldt.exe.xyz` (provisioned 2026-08-01; currently bare).
**Written:** 2026-09-09.

This is the runbook. §12 says *what* and *why*; this says *how*, in the order it has to
happen. It is also the reference implementation for the credential-scoping pattern —
`Code/incidents/2026-09-09-c3po-github-token-scope.md` points here.

---

## 1. What this achieves

1. Autonomous operation stops depending on the laptop being awake.
2. Supervision stops depending on a terminal — the console is reachable at a URL.
3. A compromise of any one service stops being a compromise of everything.

Point 3 is the one that constrains the design, so it is worth stating the target
plainly: **after this plan, an attacker with code execution in the console process gets
the Humboldt repository and nothing else.** Not the Discord identity, not the Anthropic
bill, not the Pinecone indexes, not the VM, not other repos, not the exe.dev account.

---

## 2. Current state and why it is not acceptable to deploy onto

The VM today is bare: `exedev`, passwordless sudo, no services, no keys. Deploying the
obvious way — clone into `~exedev`, one `.env`, two systemd units as `exedev` — would
produce exactly the arrangement that is live on `c3po-vm` today and is the subject of the
incident above. Specifically it would give a web-reachable console: passwordless sudo,
the Discord bot token, the Anthropic key, and a GitHub credential.

The extra work below is small and is the entire point of doing the cutover deliberately.

---

## 3. Users and layout

Three identities, none of them `exedev`:

| user | runs | sudo |
|---|---|---|
| `humboldt-daemon` | `humboldt-daemon.service` | none |
| `humboldt-console` | `humboldt-console.service` | none |
| `exedev` | nothing | keep (operator's own admin path) |

```
/srv/humboldt/repo/           the checkout — group humboldt, g+w, both users
/etc/humboldt/daemon.env      chmod 600, owned humboldt-daemon
/etc/humboldt/console.env     chmod 600, owned humboldt-console
```

**Env files live outside the checkout, deliberately.** The repo is group-shared so both
services can write to the working tree; anything inside it is therefore readable by both.
`.env` at the repo root — how the laptop does it — would hand the console the daemon's
keys and defeat the split. systemd `EnvironmentFile=` sets real environment variables,
and `python-dotenv`'s `load_dotenv()` does not override already-set variables, so the
code needs no change.

```bash
sudo groupadd humboldt
sudo useradd -r -M -g humboldt -s /usr/sbin/nologin humboldt-daemon
sudo useradd -r -M -g humboldt -s /usr/sbin/nologin humboldt-console
sudo install -d -o humboldt-daemon -g humboldt -m 2775 /srv/humboldt
sudo install -d -o root -g root -m 0755 /etc/humboldt
git config --global --add safe.directory /srv/humboldt/repo
# setgid (2775) so files created by either service stay group-owned and group-writable
cd /srv/humboldt/repo && git config core.sharedRepository group
```

---

## 4. Credentials

### 4.1 The split

Only one secret is shared. This is what makes the two-user split worth doing.

| | daemon.env | console.env |
|---|---|---|
| `ANTHROPIC_API_KEY` | ✓ | |
| `VOYAGE_API_KEY` | ✓ | |
| `PINECONE_API_KEY`, `PINECONE_C3PO_HOST`, `PINECONE_HUMBOLDT_HOST` | ✓ | |
| `DISCORD_BOT_TOKEN` + the four Discord ids | ✓ | |
| `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` | ✓ | |
| `C3PO_WORKER_URL`, `C3PO_MCP_KEY` | ✓ | |
| GitHub push | own scoped PAT | own scoped PAT |

The console needs no model, vector, chat or deploy credential. It edits YAML and commits.
If a future console feature appears to need one of these, that is a signal the feature
belongs in a behaviour the daemon runs, not in the console.

### 4.2 GitHub credentials — scoped PAT, because deploy keys are unavailable

**Do not use `gh auth login`.** That authenticates as the account and reaches every repo
the account can reach — incident 2026-09-09-01, where exactly that arrangement on
`c3po-vm` held admin and push on every Protocol-Institute repo *and* on personal repos.

**Corrected 2026-09-09.** This section previously specified two per-repo deploy keys.
That is not executable here: while remediating the c3po incident, `POST /repos/{repo}/keys`
returned **`422 Deploy keys are disabled for this repository`** for all three PI repos,
and succeeded on a personal repo — the restriction is an org-wide policy on
Protocol-Institute. Deploy keys remain the better primitive in principle (bound to one
repo by GitHub, unwidenable), so revisit if that policy is ever relaxed.

**What to use instead**, matching what c3po landed on: **a fine-grained PAT scoped to
`Protocol-Institute/humboldt` only, `Contents: write` and nothing else.** No admin, no
other repositories, no personal repositories, and a fixed expiry.

The properties this must preserve, which are the reason the section existed:

- **One repo.** The scope selector, not the token type, is where privilege lives — a
  fine-grained PAT issued against *All repositories* is functionally a classic PAT while
  looking like the safe kind. That misreading is the root cause in the c3po incident.
- **Contents: write only.** Enough to push; not enough to open a PR, change settings, or
  read anything else. If some future need appears to require more, prefer moving that
  work into a GitHub Actions workflow with its own `GITHUB_TOKEN` — which is how c3po
  removed its PR-creation need rather than re-granting the permission.
- **An expiry.** A credential that never expires is one nobody ever revisits.

**One token or two?** Two deploy keys were specified so console access could be revoked
without stopping the daemon. Two PATs give the same property and are worth it for the same
reason; if that is judged not worth the management overhead, one shared token is
acceptable *provided* §3's user split still holds, since the file is then readable by both
service users and the split stops bounding the blast radius at the credential.

Store the token in the per-service env file (`/etc/humboldt/{daemon,console}.env`,
`chmod 600`), never in a remote URL, and configure git to read it from there. Record it in
`protocol-institute/admin/keys.md` with the VM as deployment location, per the PI key
policy — and record the token that is **actually deployed**: the c3po incident found the
registry describing a narrow credential while the VM ran an entirely different, wide one.

Set a distinct git identity per service so `git log` shows which one wrote:

```bash
git config user.name  "humboldt-daemon"   # and humboldt-console respectively
git config user.email "daemon@humboldt.invalid"
```

Note this makes `[console]`-tagged commits attributable to a real actor for the first
time; today they are indistinguishable from laptop commits.

---

## 5. systemd units

Both `Restart=always`, logs to journald, no `nohup`/`tmux`. Hardening directives are
cheap here and directly bound the blast radius:

```ini
[Service]
User=humboldt-console
Group=humboldt
EnvironmentFile=/etc/humboldt/console.env
WorkingDirectory=/srv/humboldt/repo
ExecStart=/srv/humboldt/repo/.venv/bin/python3 -m agent.humboldt console --port 7878 --no-open --push
Restart=always

NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/srv/humboldt/repo
ProtectKernelTunables=true
ProtectControlGroups=true
RestrictSUIDSGID=true
```

`ProtectSystem=strict` + `ReadWritePaths` means the console can write the checkout and
nothing else on the filesystem. `NoNewPrivileges` blocks setuid escalation even if a sudo
rule is added later by mistake.

The daemon unit is the same shape with `User=humboldt-daemon`,
`EnvironmentFile=/etc/humboldt/daemon.env`, and `ExecStart=… daemon run`.

---

## 6. Console exposure

```bash
ssh exe.dev share port    humboldt 7878   # proxy → the console port
ssh exe.dev share set-private humboldt    # confirm; private is the default
ssh exe.dev share add     humboldt <supervisor-email>   # web-only, no --root
ssh exe.dev share show    humboldt        # verify: Mode Private, expected shares only
```

Reached at `https://humboldt.exe.xyz`, authenticated by exe.dev. No Cloudflare Tunnel, no
Pages Function, no D1 binding — see §12.2b for why that route was dropped.

Never `--root`: that grants shell and sudo, and supervision needs neither.

### 6.1 Console hardening — required before exposure

The console was written for localhost and authenticates nobody. Three changes, all in
`agent/console.py`, all blocking:

1. **Require a shared secret.** exe.dev's proxy is the outer door, not the only one. The
   console should reject any request lacking a token it reads from `console.env`, so that
   a stray `set-public` is not instantly an open console.
2. **Record the acting supervisor.** The approval queue's whole value is that a human
   approved something; it currently records no identity. Capture whatever the proxy
   forwards and write it into the queue entry and the `[console]` commit trailer.
3. **Protect state-changing requests.** Every mutation is a POST today with no CSRF
   defence, which was fine on localhost and is not fine behind a browser-reachable URL.

---

## 7. Verification

Run after cutover, then on a `systemd` timer so a credential widened later is caught
rather than discovered. These are the assertions from `Code/warnings-exe.md` policy 6.

```bash
# 1. the VM cannot reach the exe.dev account
ssh -o BatchMode=yes exe.dev whoami                      # must FAIL

# 2. the token reaches exactly one repo, and only to write contents
curl -sf -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/repos/Protocol-Institute/humboldt >/dev/null   # must SUCCEED
curl -so /dev/null -w '%{http_code}' -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/repos/Protocol-Institute/website               # must be 404
# and it must not be able to act on the repo beyond contents:
curl -so /dev/null -w '%{http_code}' -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/repos/Protocol-Institute/humboldt/collaborators # must be 403/404

# 3. no account-scoped GitHub credential exists on the box
which gh && gh auth status 2>&1 | grep -q "Logged in" && echo "FAIL: gh is authenticated"

# 4. neither service user can escalate
sudo -u humboldt-console sudo -n true 2>&1 | grep -q . && echo "ok: no sudo"

# 5. the console cannot read the daemon's secrets
sudo -u humboldt-console cat /etc/humboldt/daemon.env 2>&1 | grep -q "Permission denied" \
  && echo "ok: split holds"
```

Test 5 is the one that proves the split actually works, rather than merely being
configured. Run it explicitly — it is the difference between a documented property and a
verified one.

---

## 8. Cutover sequence

1. Provision users, directories, env files, scoped tokens (§3–4). Do not start services.
2. Clone, create `.venv`, install deps. Verify `laws validate all` and
   `analytics utilization` run as `humboldt-console`.
3. Run §7 verification **before** exposing anything. Fix failures now.
4. `daemon pause` on the laptop; stop and unload the laptop launchd plist.
5. Start `humboldt-daemon.service`; confirm Discord presence and one clean task tick in
   journald.
6. Start `humboldt-console.service`; reach it over the SSH tunnel first (`ssh
   humboldt-console`) — the tunnel is not retired, only demoted from being the only route.
7. Apply §6.1 console hardening. Only then `share port` / `share add`.
8. `daemon unpause` **on the VM**.
9. Re-run §7. Record the VM as a deployment location in `../admin/keys.md`; update the
   inventory row in `Code/warnings-exe.md`.

**Rollback:** stop both units, unpause the laptop daemon, revoke the tokens on GitHub. The repo is the source of truth and the VM holds no unique state, so rollback
costs only the time since cutover.

---

## 9. Explicitly out of scope

- The Phase 5 Discord quiet-mode rework (§9) — a separate work item that happens to share
  the phase.
- Merging `redesign-2026-08` to `main`. The merge is a Phase 5 milestone but is not part
  of this runbook and should not be bundled into the same change.
- Retiring the SSH tunnel. It stays as the fallback path and for anything needing a shell.
