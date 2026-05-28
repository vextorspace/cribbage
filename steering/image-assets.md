# Image assets catalog

The friend group has produced AI-generated joke art over the course of the WhatsApp chat.
These are now the canonical "official ICA portraits, photographs, and tournament
documentation" for the site. The files live in `evidence/` (gitignored) — copy them into
`cribbage/static/cribbage/images/` (renamed for clarity) before referencing them in
templates.

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

## Asset gaps (need to source separately)

- **Pat Thornenberg portrait** — Pat is fictional, no source image exists. Generate
  a dignified AI portrait of a middle-aged-male federation administrator, suit-and-tie,
  serious expression, slightly bureaucratic
- **Bart portrait** — likewise fictional. Generate an older male portrait, official
  dress, perhaps shown removed from a wall (a faint outline where the frame hung)
- **Michelle Cullen portrait** — real person; needs her consent before any photo or
  AI likeness goes on the site. If consent isn't available, **omit her photo entirely**
  and use a respectful placeholder (e.g. a silhouette with caption "Director of Special
  Programs; no portrait available")
- **Tim portrait** — same consent issue; same fallback
- **Katrina portrait** — same consent issue; same fallback
- **Doug Ronne portrait** — the user himself; he can provide one or we generate one
- **ICA crest / logo** — needs to be designed from scratch (see design.md)
- **Suckling House (The Hague HQ)** — needs an exterior photo or AI-generated rendering
  of a dignified Lange Voorhout building
- **Generic news thumbnails** — committee meetings, gavels, tournament halls, etc.
