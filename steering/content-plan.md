# Content plan

The site's content is the joke. Treat copy with as much care as code.

## Pages (initial scope)

| Route | Template | Purpose |
| --- | --- | --- |
| `/` | `home.html` | Hero, "President's Welcome," featured news, upcoming "events" |
| `/rules/` | `rules.html` | The actual rules of cribbage, presented as if codified by the ICA |
| `/news/` | `news.html` | Joke news stories, listed newest-first |
| `/news/<slug>/` | `news_detail.html` | Individual story (if we want permalinks) |
| `/about/` | `about.html` | Org history, made-up board of directors, founding date |
| `/contact/` | `contact.html` | Fictitious HQ address, registration form that does nothing |

## Rules section

Should be **genuinely accurate** rules of cribbage. The joke is the framing (formal bylaws,
section numbers, footnotes about "Resolution 1947-B regarding the disputed nineteen-hand"), not
incorrect rules. A reader who wants to learn cribbage from this page should succeed.

Sections to cover:
- The deal and the crib
- The play (pegging) — 15s, pairs, runs, last card
- The show — counting hands and the crib
- Scoring tracks, "skunks," "double skunks"
- Variations (3-hand, 4-hand partners) noted as "ratified variants"

## News stories

Tone reference: dry wire-service copy (Reuters/AP), not satire that announces itself. The
narrative spine is **Tony and Alicia's rise to the top of the Association followed by their
fall in the Equine Scandal** — see the full arc and 16-story list in
[canon.md → The Equine Scandal](canon.md).

Each story is its own template under `templates/cribbage/news/<slug>.html`, ~250–400 words,
written as straight wire copy. The listing on `/news/` shows the scandal stories at the
top; the rise stories sit below and in archive view.

Voice notes when quoting:
- **Pat Thornenberg** — escalating-synonym lists ("STOP, CEASE, DESIST, DISCONTINUE…"),
  invocations of "the small children" and global stakes, citations of fictional bylaw
  subsections (e.g. "section 16.174.22.3, paragraph 14.d")
- **Alicia Lake** — grandiose claims wrapped in performative humility, frequent appeals to
  "all of humanity" and "the small children that look up to" the top players
- **Tony Cullen** — apparent humility while actually self-aggrandizing; deploys
  *"allegedly"* as a load-bearing word in any reference to the kicking incidents
- **Michelle Cullen** — never speaks in the press; the wire copy notes only that she
  "declined to comment" and continues her Uganda work
- **Bystanders / wire correspondents** — neutral, sober, professional

Every story ends with the **Ronne footnote**: a single sentence noting that Mr. Ronne
(Pi Level, 3.14) remains the lowest-ranked individual ever inducted and has not progressed.

## Recurring fake-org elements

All canon facts (founding year, HQ, Pat's bio, motto, crest) live in
**[canon.md](canon.md)**. Read that before writing any page copy. Summary:

- Founded 1893 (London) → renamed/reorg 1923 → relocated to The Hague 1946
- HQ: The Hague, Netherlands
- Executive Director: Dr. Patrycja Lindqvist-Okafor (since 2014) — long bio on About page
- President: Eduard Margolis (Latvia, elected 2022)
- Motto: *Quindecim duo*

## News story authoring

Each news story is its own template file under `templates/cribbage/news/`, with the
listing page (`news.html`) hard-coding the index of stories. To add a story: create
`templates/cribbage/news/<slug>.html`, then add an entry to the news index list in
`views.py`.

## Graphics

- Hero image: green felt cribbage board, dramatic lighting
- Logo / crest: heraldic, dignified
- Section headers: subtle card-suit motifs
- News thumbnails: stock-photo style (committee meetings, gavels, trophies)

Decide source: stock-photo licenses, AI image generation, or commissioned/hand-drawn. List
sources in `steering/assets.md` when chosen.
