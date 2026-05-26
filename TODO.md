# Developer TODO — Tracks 2 and 3

Infrastructure, persona, and template work. This is the *operator* layer — managing Humboldt as a project. Humboldt's own research agenda is in `research/agenda.md`.

Priority: **[H]** urgent, **[M]** soon, **[L]** when convenient.

---

## Track 2 — Persona and Infrastructure

### Discord presence quality (next cluster)

- **[H]** **Conversation style tuning** — review actual #new-nature transcripts and identify what's off. Current symptoms: likely too formal / too long / too eager. Tune `_slim_context()` and `_rich_context()` prompts based on observed output. May require a dedicated prompt-tuning session with real examples.

- **[H]** **Idea and reference capture from Discord** — when Humboldt participates in a conversation, it should notice and save: (1) ideas or arguments that bear on its research hypotheses, (2) external papers/articles/links that participants cite. Save to `inbox/` as structured items. This is the "input → inventory" flow that was deferred at Discord launch. Design: detect in `on_message` and `task_new_nature` response path; use a lightweight extraction call (Haiku) to decide if anything is worth saving before responding.

- **[M]** **Discord user models** — gradually build mental models of frequent interactors: their interests, background, recurring themes in their posts, prior exchanges with Humboldt. Store in `daemon/user_models.yaml` (gitignored — personal, not public). Use in `generate_mention_response` to personalize responses and acknowledge history. Update after each meaningful exchange.

- **[M]** **Richer self-context in Discord responses** — current `_rich_context()` includes laws and hypotheses but not the research agenda, LINEAGE.md in full, or recent open questions. Humboldt should be able to situate a conversation within its actual current thinking, not just inventory. Add agenda summary and current open questions to rich context.

### Daemon infrastructure

- **[M]** **Daemon auto-restart on code changes** — currently requires manual kill + restart after every code change. Add `--reload` dev mode or use `watchdog` to restart on file change. Low priority for always-on deployment, higher priority during active development.

- **[L]** **Always-on machine deployment** — move daemon to a machine that doesn't sleep. Write systemd unit file; add `git pull` + restart on schedule so code updates deploy automatically.

- **[L]** **Thread support** — `task_new_nature` only reads main channel, not threads. Threads require explicit @mention currently. Decide whether to extend the proactive check to threads or leave @mention as the thread entry point.

---

## Track 3 — Artificial Researcher Template

- **[M]** Update `_template/` to reflect current architecture (IDENTITY/LINEAGE/MEMORY/METHOD/BOOTSTRAP) — `SOUL-template.md` is superseded.
- **[M]** Add ingest pattern to template — augmented chunk text (title+section prefix) is the generalizable design decision; capture in `_template/`.
- **[L]** Copy M-001 through M-003 to `_template/methods/` in generic form — strip PI specifics.
- **[L]** Write `_template/CLAUDE-template.md` — generic Claude Code setup for AR projects.
- **[L]** Extract as separate repo when stable — threshold: 5+ sessions, pattern tested, reviewed.
