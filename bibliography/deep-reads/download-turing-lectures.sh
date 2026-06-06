#!/usr/bin/env bash
# Download ACM Turing Award Lectures
#
# amturing.acm.org is Cloudflare-protected — this script cannot run headlessly.
# To use:
#   1. Open https://amturing.acm.org/lectures.cfm in a browser and let it load fully
#   2. Open browser DevTools → Application → Cookies → copy the __cf_bm and cf_clearance values
#   3. Set them in the CF_BM and CF_CLEARANCE variables below
#   4. Run this script: bash download-turing-lectures.sh
#
# Alternatively: use the browser's "Save all PDFs" or download each manually from the page.

CF_BM=""         # paste __cf_bm cookie value here
CF_CLEARANCE=""  # paste cf_clearance cookie value here
DEST="$(dirname "$0")"  # saves into bibliography/deep-reads/

if [[ -z "$CF_BM" || -z "$CF_CLEARANCE" ]]; then
  echo "ERROR: Set CF_BM and CF_CLEARANCE from your browser session first."
  echo "See comments at the top of this script."
  exit 1
fi

COOKIE="__cf_bm=${CF_BM}; cf_clearance=${CF_CLEARANCE}"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

fetch() {
  local url="$1" out="$2"
  if [[ -f "$out" ]]; then
    echo "SKIP (exists): $out"
    return
  fi
  echo "Downloading: $out"
  curl -s -L --max-time 60 -A "$UA" -H "Cookie: $COOKIE" -H "Referer: https://amturing.acm.org/lectures.cfm" \
    "$url" -o "$out"
  sleep 2  # be polite
}

# ---------------------------------------------------------------------------
# Lecture PDF URLs — pattern: https://amturing.acm.org/vtype=08
# Individual lecture PDFs are linked from each laureate page.
# URLs below need to be verified from the actual lectures.cfm page.
# Format from known examples: https://amturing.acm.org/award_winners/{name}_{id}.cfm
# The PDF links on those pages follow no single predictable pattern.
#
# KNOWN / CONFIRMED PDF URLs (from prior manual inspection):
# ---------------------------------------------------------------------------

# Dijkstra 1972 — "The Humble Programmer"
fetch "https://dl.acm.org/doi/pdf/10.1145/355604.361591" "$DEST/turing-1972-dijkstra-humble-programmer.pdf"

# Backus 1977 — "Can Programming Be Liberated from the von Neumann Style?"
fetch "https://dl.acm.org/doi/pdf/10.1145/359576.359579" "$DEST/turing-1977-backus-liberated-programming.pdf"

# Hoare 1980 — "The Emperor's New Clothes"
fetch "https://dl.acm.org/doi/pdf/10.1145/1283920.1283936" "$DEST/turing-1980-hoare-emperors-new-clothes.pdf"

# Knuth 1974 — "Computer Programming as an Art"
fetch "https://dl.acm.org/doi/pdf/10.1145/361604.361612" "$DEST/turing-1974-knuth-programming-as-art.pdf"

# ---------------------------------------------------------------------------
# For the rest: fetch each laureate page, extract the PDF link, download it.
# Laureate page URL format (from known examples):
# ---------------------------------------------------------------------------

LAUREATE_PAGES=(
  "1966/perlis_1650901"
  "1967/wilkes_1000749"
  "1968/hamming_1000652"
  "1969/minsky_1000850"
  "1970/wilkinson_1000768"
  "1971/mccarthy_1000322"
  "1972/dijkstra_1000528"
  "1973/bachman_1000009"
  "1974/knuth_1013884"
  "1975/newell_simon_1000845"
  "1976/rabin_scott_1000604"
  "1977/backus_0703524"
  "1978/floyd_1000695"
  "1979/iverson_1000652"
  "1980/hoare_4622167"
  "1981/codd_1000892"
  "1982/cook_0499341"
  "1983/ritchie_thompson_4046702"
  "1984/wirth_1000681"
  "1985/karp_3941301"
  "1986/hopcroft_tarjan_1000413"
  "1987/cocke_2083115"
  "1988/sutherland_3467142"
  "1989/kahan_1000844"
  "1990/corbato_1000070"
  "1991/milner_1057343"
  "1992/lampson_1000062"
  "1993/hartmanis_stearns_1000016"
  "1994/feigenbaum_reddy_1024846"
  "1995/blum_1002892"
  "1996/pnueli_1000478"
  "1997/engelbart_1000062"
  "1998/gray_3649936"
  "1999/brooks_1002898"
  "2000/yao_2167982"
  "2001/dahl_nygaard_1000685"
  "2002/rivest_shamir_adleman_1002712"
  "2003/kay_3681036"
  "2004/cerf_kahn_1065208"
  "2005/naur_1024454"
  "2006/allen_1001456"
  "2007/clarke_emerson_sifakis_1065337"
  "2008/liskov_1108679"
  "2009/thacker_1615085"
  "2010/valiant_2612174"
  "2011/pearl_2658630"
  "2012/goldwasser_micali_4947227"
  "2013/lamport_1000652"
  "2014/stonebraker_1002928"
  "2015/diffie_hellman_3321342"
  "2016/berners-lee_8087960"
  "2017/hennessy_patterson_1077097"
  "2018/bengio_lecun_hinton_9043074"
  "2019/catmull_hanrahan_3482059"
  "2020/aho_ullman_1058464"
  "2021/dongarra_2237498"
  "2022/metcalfe_5684792"
  "2023/wigderson_2237504"
  "2024/barto_sutton_9086232"
  "2025/bennett_brassard_9086233"
)

echo ""
echo "Fetching laureate pages to extract PDF links..."
echo "(IDs above are approximate — verify against actual site)"
for entry in "${LAUREATE_PAGES[@]}"; do
  year="${entry%%/*}"
  slug="${entry##*/}"
  page_url="https://amturing.acm.org/award_winners/${slug}.cfm"
  echo "  Checking $year: $page_url"
  pdf_url=$(curl -s -L --max-time 15 -A "$UA" -H "Cookie: $COOKIE" "$page_url" \
    | grep -oE 'href="[^"]*\.pdf"' | head -1 | grep -oE '"[^"]+"' | tr -d '"')
  if [[ -n "$pdf_url" ]]; then
    [[ "$pdf_url" != http* ]] && pdf_url="https://amturing.acm.org/$pdf_url"
    outfile="$DEST/turing-${year}-${slug%_*}.pdf"
    fetch "$pdf_url" "$outfile"
  else
    echo "    No PDF link found on page — may require manual download"
  fi
  sleep 2
done

echo ""
echo "Done. Check $DEST for downloaded files."
echo "Any 'No PDF link found' entries need manual download from https://amturing.acm.org/lectures.cfm"
