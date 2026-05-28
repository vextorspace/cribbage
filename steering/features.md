# Interactive features

In addition to the static content described in [content-plan.md](content-plan.md), the v1
site includes three interactive features. All three are framed as official services of the
Association — never break that framing.

## 1. Membership registration form

Route: `/membership/apply/`

A multi-field application form for "Individual Associate Membership in the ICA."

- Fields: full name, nationality, mailing address, years playing cribbage, preferred
  variant (standard 2-hand / 3-hand / 4-hand partners), national federation affiliation
  (dropdown of 87 invented members + "None"), and a 500-character "Statement of Intent"
  textarea.
- Submission: form posts, server validates, then renders a serious confirmation page:
  *"Your application has been received and assigned reference number ICA-2026-XXXXXX.
  Applications are reviewed quarterly by the Membership Committee. Please allow
  6–8 weeks for a determination."*
- Data: **do not store submissions.** Reference number is randomly generated per
  request. (If we ever want to store them as a gag, document the privacy implications
  first — even a joke site collecting PII is a real liability.)
- No emails sent. No follow-up. The void is the joke.

## 2. Official Scoring Engine (hand calculator)

Route: `/scoring/calculator/`

Framed as "the ICA Official Scoring Engine, used by Tribunal adjudicators in all
sanctioned competitions."

Functionality:
- User selects 4 hand cards + 1 cut card (the "starter")
- Optionally: indicate whether scoring the crib (affects flush rules — crib flush
  requires the starter to match)
- Calculator reports a breakdown:
  - Fifteens (every combination summing to 15, 2 pts each)
  - Pairs (every pair of matching ranks, 2 pts; three-of-a-kind = 6, four = 12)
  - Runs (longest run wins, counted by length × multiplicity for doubled runs)
  - Flushes (4-card if all hand cards same suit = 4, +1 if starter matches; crib only
    counts 5-card flush)
  - Nobs (jack in hand matching starter's suit = 1 pt)
  - Total

Implementation:
- Pure client-side JavaScript — no server round-trip
- Card picker UI: 4 + 1 grid of rank/suit selectors (start with text dropdowns,
  upgrade to card-art later)
- Tested. Cribbage scoring is well-defined; a wrong scorer is embarrassing for a
  joke that depends on looking authoritative.
- Test cases: include the canonical 29 hand (5-5-5-J + cut 5 of J's suit) and a few
  zero-point hands.

## 3. Tournament & events calendar

Route: `/events/`

A static list of upcoming sanctioned events, presented as a federation calendar.

- 8–15 fictitious events spread across the next 18 months
- Each entry: date, host city, event name, sanctioning level
  (World Championship / Continental / National Open / Regional Qualifier),
  brief description, "registration closed" or "via national federation" link
- Examples:
  - "World Pairs Championships 2026 — Reykjavík, 14–18 September"
  - "Pan-American Open — Mexico City, 22–24 November"
  - "Suckling Memorial Invitational — Norwich, 12 January 2027"
- No actual registration. Calendar is informational copy only.

Data structure:
- Hard-code as a Python list in `views.py` or a separate `events.py` module
- No DB, no admin. To add an event, edit the file and redeploy.

## Out of scope for v1

These have come up in brainstorming but are not in v1:

- User accounts / login
- Comments on news stories
- Search
- Multi-language (canon mentions Pat speaking 7+ languages, but the site is English-only)
- A live "Rankings" page (would need data, ongoing curation)
- Merchandise / store
