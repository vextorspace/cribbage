# Image assets catalog

The friend group has produced AI-generated joke art over the course of the WhatsApp chat.
These are now the canonical "official ICA portraits, photographs, and tournament
documentation" for the site. The files live in `evidence/` (gitignored) — copy them into
`cribbage/static/cribbage/images/` (renamed for clarity) before referencing them in
templates.

## Working reference: static files → bulletin assignments

The table below is the day-to-day lookup when adding images to a news bulletin.
It indexes the files **as they exist in `static/cribbage/images/`** (not by their
WhatsApp source names) and points each to the bulletin slug(s) where it would
naturally appear, with a short in-universe gloss for the caption.

The "source catalog" sections further down still hold the original chat context
and are the right place to look when adding *new* images from `evidence/`.

### Primary bulletin assignments (strong one-to-one matches)

| Static file | Bulletin slug | One-line in-universe gloss |
| --- | --- | --- |
| `register/lake-washington-state-finals-perfect-29.jpg` | `lake-perfect-29-washington` | Ms. Lake at the closing leg of the Washington State Finals; the eighth sanctioned twenty-nine of her career. |
| `register/lake-huge-gesture-bulletin.jpg` | `lake-perfect-29-washington` (companion / morning-after) | Ms. Lake at the close of a substantial gesture undertaken the morning following the Finals; particulars known only to the Sector Secretariat. |
| `register/ronne-on-tender-maintenance.jpg` | `ronne-2025-title-confirmed` | Mr. Ronne in the main cabin of the Cullen family tender, mid-overhaul; the wrench held aloft by tradition. |
| `register/bahamian-engagement-at-sunset.jpg` | `ronne-2025-title-confirmed` (atmospheric) | A sanctioned vessel of the Cullen family at sunset; the Convening Rule was, at this hour, in force. |
| `register/cullen-hall-of-champion-portrait.jpg` | `thornenberg-suspensions` or `ronne-2025-title-confirmed` | Mr. Cullen's IWCCA Hall of Champion portrait, presently tarpaulined at Council recommendation. |
| `register/lake-divine-portrait-iwcca.jpg` | `lake-revival-staged` | Ms. Lake in the (figurative) divine pose; oil on canvas, IWCCA commission, MMXXV. |
| `register/lake-portrait-alternative-take.jpg` | `lake-revival-staged` (counter-evidence) | The alternative attribution of the divine composition, submitted to the Office of the Director by Mr. Ronne. |
| `register/equine-cousin-roadside.jpg` | `tribunal-opens-equine-inquiry` or `veterinary-linguist-thirty-one` | An equine cousin of the present proceedings, photographed roadside in the Eleuthera district; no standing in any sanctioned engagement. |
| `tribunal-exhibits/exhibit-014-a.jpg` … `-e.jpg` | `tribunal-opens-equine-inquiry`, `lake-revival-staged`, `veterinary-linguist-thirty-one` (cite as evidence) | Photographic evidence of unsanctioned equine engagements; full series catalogued on the Tribunal Exhibits page. |

### Secondary / multi-bulletin candidates

| Static file | Candidate bulletin slug(s) | One-line in-universe gloss |
| --- | --- | --- |
| `register/lake-official-portrait-monalicia.jpg` | `lake-mentee-induction`, `cullen-lake-masters-dubai`, `lake-revival-staged` | Ms. Lake's standing official portrait ("Monalicia"); oil on canvas, anonymous, MMXXIV. |
| `register/cullen-africa-order-of-canada.jpg` | future "Exit Strategy" bulletin; or `thornenberg-suspensions` (contextual) | Mr. Cullen on East African sabbatical, decorated with what Ms. Lake identified at the time as the Order of Canada. |
| `register/cullen-engagement-january-mmxxvi-a.jpg` | `cullen-lake-masters-dubai` (era-adjacent) or archive | Mr. Cullen at a sanctioned engagement, January MMXXVI. From the Secretariat archive. |
| `register/cullen-engagement-january-mmxxvi-b.jpg` | as above (companion frame) | Mr. Cullen at a sanctioned engagement, January MMXXVI. From the Secretariat archive. |
| `register/champion-nutritional-supplement.jpg` | `lake-perfect-29-washington` or `tarbish-tournament-lake` (champion-lifestyle aside) | The Association's standing nutritional supplement for sanctioned champions; composition presently undisclosed. |

### Atmospheric / archive-only (no bulletin assignment yet)

| Static file | Suggested home | One-line in-universe gloss |
| --- | --- | --- |
| `register/bahamian-engagement-kayak.jpg` | Photographic Register only | A member of the Spanish Wells expedition party at the eastern cays; identification not yet settled by the archivist. |
| `register/bahamian-engagement-grotto.jpg` | Photographic Register only | A member of the Bahamian expedition party at the eastern grotto; identification, again, unsettled. |
| `register/cullen-holiday-greeting-mmxxv.jpg` | Photographic Register / future seasonal bulletin | Mr. Cullen's annual seasonal greeting to the federated game, MMXXV. |
| `register/katrina-tim-cribbage-board-donation.jpg` | future Donors / Patrons page | The inlaid rosewood cribbage board donated by Patrons Katrina and Tim; peg holes positioned by tradition. |

### Already placed in a bulletin

| Static file | Placed in | Notes |
| --- | --- | --- |
| `spanish-wells-cullen-portrait.jpg` | `cullen-spanish-wells-pigs` | First of three figures in the bulletin. |
| `spanish-wells-cullen-volunteer.jpg` | `cullen-spanish-wells-pigs` | Second figure. |
| `spanish-wells-lake-visit.jpg` | `cullen-spanish-wells-pigs` | Third figure. |

### Bulletins with no image candidate at present

The following bulletins have no obvious match in the current `static/` set and
will either need a generic atmospheric asset (committee chamber, gavel, tournament
hall) or can stand without imagery: `cullen-level-1-toronto`,
`cullen-level-3-helsinki`, `cullen-uganda-tiny-homes`, `lake-trudeau-rcmp-ruling`,
`tarbish-tournament-lake`.



Confirmed viewed (representative):

- **"Monalicia"** — Alicia Lake's face on a Mona Lisa-style oil painting, holding a
  cribbage hand (5♣ 6♥ 9♠) with a board in front of her and a Da Vinci landscape behind.
  → **Director of Mentorship official portrait** on the About / Lake bio page.
  Source: `WhatsApp Image 2026-01-29 at 08.22.20.jpeg` (chat: "the monalicia")

## Catalog (cross-referenced from `_chat.txt` timestamps)

| File | Chat context | Suggested site use |
| --- | --- | --- |
| `WhatsApp Image 2025-12-18 at 07.24.16.jpeg` | Tony's Dec greeting image | Tony bio / archive |
| `WhatsApp Image 2026-01-02 at 16.25.50.jpeg` | Tony: "code program I wrote for chat gpt that interprets the future" | Hall of Champion — Cullen portrait |
| `WhatsApp Image 2026-01-03 at 09.03.22.jpeg` | Alicia: "the original from Pat" — the divine-pose painting (Sistine-style) | IWCCA archive / Lake page secondary image |
| `WhatsApp Image 2026-01-03 at 19.15.02.jpeg` | Doug: "this is closer to what actually happened" — alt take | Tribunal evidence appendix / Lake page |
| `WhatsApp Image 2026-01-06 at 11.42.55.jpeg` | Tony shared image (1 of 3) | Tony archive |
| `WhatsApp Image 2026-01-06 at 11.42.55 (1).jpeg` | Tony shared image (2 of 3) | Tony archive |
| `WhatsApp Image 2026-01-09 at 18.55.16.jpeg` | Tony "in Africa, developing an exit strategy from the cribbage stronghold" — wearing what Alicia identifies as an Order of Canada medal | **Tony bio hero** / "Exit Strategy" news story |
| `WhatsApp Image 2026-01-19 at 18.53.20.jpeg` | Alicia: "Another big win. Washington State finals!!! Ever see a perfect score!" | **"Lake Wins Washington State Finals With Perfect 29" news story** |
| `WhatsApp Image 2026-01-19 at 20.20.56.jpeg` | Alicia: "I made a huge gesture, which you will probably read about tomorrow" | Lake rise-era story |
| `WhatsApp Image 2026-01-20 at 08.03.16.jpeg` | Alicia's "busy weekend that was" — dead horse photo (1 of 5) | **Equine Scandal evidence — Tribunal exhibit** |
| `WhatsApp Image 2026-01-20 at 08.03.16 (1).jpeg` | Dead horse weekend (2 of 5) | Equine Scandal Tribunal exhibit |
| `WhatsApp Image 2026-01-20 at 08.03.17.jpeg` | Dead horse weekend (3 of 5) | Equine Scandal Tribunal exhibit |
| `WhatsApp Image 2026-01-20 at 08.03.17 (1).jpeg` | Dead horse weekend (4 of 5) | Equine Scandal Tribunal exhibit |
| `WhatsApp Image 2026-01-20 at 08.03.42.jpeg` | Dead horse weekend (5 of 5) | Equine Scandal Tribunal exhibit |
| `WhatsApp Image 2026-01-29 at 08.22.20.jpeg` | "Monalicia" — Alicia as Mona Lisa with cribbage hand and board | **Lake official portrait** (About page hero) |
| `WhatsApp Image 2026-03-31 at 16.25.59.jpeg` | Katrina and Tim's gift crib board ("Guess where the pegs go") | **Donors / Patrons page** — Katrina & Tim acknowledgement |
| `WhatsApp Image 2026-05-18 at 15.11.57.jpeg` | "Nutritious substance made for true champions" (the one Alicia let Doug eat) | Lake rise-era story / champion lifestyle archive |

## Spanish Wells / Bahamas trip, 2023

A second batch of source photographs documenting a sailing visit to the Bahamas
in early-to-mid 2023. The pig-beach photographs at Spanish Wells are the
load-bearing material for the **Michelle Cullen wild pigs** story.

| File | Subject | Suggested site use |
| --- | --- | --- |
| `seascape-sailboat-sunset-2023-01-17.jpg` | Sailboat silhouetted against sunset over open water | Atmospheric — Tony's "exit strategy" archive, or a hero image on a future Sailing Subcommittee page |
| `michelle-pigs-in-profile-2023-01-31.jpg` | **Michelle**, crouching in profile beside several wild pigs on the beach, Adirondack chairs in the background | **Spanish Wells / Wild Pigs story hero** — Michelle as the dignified caretaker |
| `alicia-pigs-to-camera-2023-01-31.jpg` | **Alicia** in orange sweater, bending toward the pigs and looking at the camera | Spanish Wells secondary — Alicia visiting Michelle's programme |
| `tony-petting-piglet-2023-01-31.jpg` | **Tony** reaching down toward a small brown piglet | Spanish Wells secondary — Mr. Cullen "lending support" to his wife's initiative |
| `kayaking-back-view-2023-04-27.jpg` | Person in straw sun hat paddling a kayak through turquoise water (face obscured) | Atmospheric — Bahamas archive |
| `douglas-with-wrench-boat-2023-04-28.jpg` | **Douglas**, blue shirt, holding up a large adjustable wrench in a boat cabin | Doug's bio page / "Director of Digital Affairs (also: shipwright apprentice)" gag |
| `grotto-cave-2023-05-07.jpg` | Person in pink shirt + sun hat + sunglasses in a grotto / sea cave (face obscured; ambiguous between Alicia and Michelle) | Atmospheric — Bahamas archive |
| `wild-donkey-roadside-2023-05-15.jpg` | Wild donkey/burro standing on a roadside in tropical scrub | Atmospheric — could illustrate a future "Tribunal Recognises Equine Cousins" footnote |

## How to use these on the site

1. Copy the file(s) you need from `evidence/` to `cribbage/static/cribbage/images/`
   with descriptive, dignified filenames (e.g. `lake-official-portrait.jpg`,
   `cullen-africa-decoration.jpg`, `tribunal-exhibit-014-a.jpg`)
2. Reference in templates with `{% static 'cribbage/images/...' %}`
3. The **static directory IS committed**, even though `evidence/` is not — so once an
   image is copied into static and renamed, it ships to the public site
4. Caption images in a sober wire-service / museum-label style:
   *"Lake, Director of Mentorship, in the official portrait commissioned by the
   IWCCA in 2024. Oil on canvas, artist anonymous."*

## Important: don't commit raw evidence images

The raw filenames in `evidence/` (e.g. `WhatsApp Image 2026-01-29 at 08.22.20.jpeg`)
reveal the source platform and the friend-group's group chat. **Only copy renamed,
captioned versions into `cribbage/static/`.** Never link to or reference the raw
`evidence/` paths in any committed code.

## Asset gaps (to generate via ChatGPT/Midjourney/etc. and drop into static/)

### Pat Thornenberg — Executive Director (androgynous)

Pat is fictional and deliberately androgynous — viewers should be unable to tell whether
this is Patrick or Patricia. Filename target: `static/cribbage/images/thornenberg-official-portrait.jpg`

**Suggested prompt:** *"A dignified official portrait, oil-painting style, of an
androgynous middle-aged person of indeterminate gender, neat short-to-medium brown hair,
wearing a charcoal suit jacket with a dark cravat, seated at a polished wooden desk with
an antique cribbage board visible at the edge of the frame, sober and slightly weary
expression, soft warm lighting, dark green velvet curtain backdrop, in the style of a
European federation's official headshot, formal and ambiguous, gender ambiguous,
no makeup, no obviously feminine or masculine features."*

The face should genuinely be ambiguous. If a first generation reads as too clearly
masculine or feminine, regenerate. The joke depends on the ambiguity holding.

### Bart Crumthwaite-Halloran — disgraced former Executive Director (fictional)

Filename target: `static/cribbage/images/crumthwaite-halloran-portrait-removed.jpg`

**Suggested prompt:** *"An empty rectangular outline on a dark green wood-paneled wall
where an oil portrait has clearly been removed — slightly lighter discoloration where the
frame sat, a small engraved brass nameplate beneath reading 'B. Crumthwaite-Halloran,
Executive Director 1998–2008', dim institutional lighting, hallway of a formal building."*

(Alternative: an actual portrait of a fictional older man in formal academic regalia,
slightly shifty expression. The "removed from wall" version is funnier and avoids
needing an actual face.)

### Real-person portraits

- **Doug Ronne** — Doug provides his own headshot, or we generate a dignified one
- **Michelle Cullen / Katrina / Tim** — default to a respectful silhouette placeholder
  with their title and a caption like *"Portrait not on file at time of publication."*
  Use a generic Director-Of-Programs-style silhouette graphic, identical for all three,
  to make their absence look like an institutional choice rather than an omission
- **Alicia Lake & Tony Cullen** — already covered by the WhatsApp joke art (they sent
  it into the chat themselves)

### Other assets

- **ICA crest / logo** — designed from scratch (heraldic shield with crossed pegs and
  six-card hand; see design.md)
- **Suckling House (The Hague HQ exterior)** — AI-generated rendering of a dignified
  Lange Voorhout building, brick or stone façade, brass plaque visible
- **Generic news thumbnails** — committee meetings, gavels, tournament halls, helicopter
  on a hotel lawn (for the helicopter-awards story), Tribunal chamber, etc.
