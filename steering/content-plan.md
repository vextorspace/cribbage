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

Tone reference: dry wire-service copy (Reuters/AP), not satire that announces itself. Drawn
from the actual evidence; see [canon.md](canon.md) for the underlying source.

Initial batch (6–10 stories, dated within the last 18 months):

- **"Cullen and Lake Elevated to Masters Level Following Sector Vote in Dubai"** —
  the inciting "promotion" from the evidence; covers Douglas Ronne's pi-level induction
- **"Helicopter Awards Delivery Mission Frustrated by Absentee Inductees; ICA Renews
  Push for Universal Chip-Implant Standard"** — Pat and Tim's hotel mission
- **"Executive Director Thornenberg Issues Statement Following Tournament Misconduct
  by D. Ronne; Tribunal Review Underway"** — the cease-and-desist email
- **"Lake Wins Washington State Finals With Perfect 29; Cites Bicycle Brand Cards
  Sponsorship"** — recent on-the-ice victory
- **"Cullen Initiative Repurposes Retired Cribbage Boards as Tiny Homes in Uganda;
  Michelle Cullen Launches Parallel Cheer Camp Program"** — the Uganda program
- **"Tribunal Examines Allegations of RCMP Misconduct at Canadian Championship Finals
  Following Lake-Trudeau Match"** — the Trudeau / political refugee storyline
- **"Hall of Champion Commissions Cullen Portrait; Artist Cites 'Centuries-Old Brushwork
  Tradition'"** — Tony's portrait
- **"Officer Tim, Born Without Tear Ducts, Moved To Tears by Cullen Correspondence;
  Confirmed as 'Truly a Miracle' by Secretariat"** — Tim's tears
- **"International Tarbish Tournament To Honour Lake as Guest; ICA Sends Observer"** —
  the Seattle tarbish event
- **"NCCWL Chair Thornenberg Reflects on 25 Years of Sanctioned Play; New Sanctioned-Wins
  Database Goes Live"** — Pat retrospective

Each story should be ~250–400 words, written as straight wire copy. Quote Pat, Tony, or
Alicia using language consistent with the evidence (e.g. Pat's escalating-synonym lists,
Alicia's invocations of "the small children" and "all of humanity," Tony's grandiose
self-assessments delivered with apparent humility).

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
