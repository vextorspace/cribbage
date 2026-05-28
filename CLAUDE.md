# International Cribbage Association (ICA) — Joke Website

A satirical "official" website for a fake international cribbage governing body, presented with the
straight-faced gravitas of a real federation (think FIFA, but for pegging and 15-2). The humor comes
from the contrast between earnest presentation and absurd content.

- **Public domain:** `www.internationalcribbageassociation.org`
- **Tone:** Dry, deadpan, bureaucratic-formal. Never wink at the camera.
- **Goal:** Look like a real association site at a glance; reveal the joke on a closer read.

## Project layout

Mirrors the `dsronne_com` reference project (standard Django `startproject` layout):

```
cribbage/
├── .github/workflows/deploy.yml
├── requirements.txt
├── cribbage/                       # outer project dir
│   ├── manage.py
│   ├── tests.py
│   └── cribbage/                   # inner package
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       ├── views.py
│       ├── wsgi.py
│       ├── asgi.py
│       ├── templates/cribbage/
│       │   ├── base.html
│       │   ├── home.html
│       │   ├── rules.html
│       │   └── news.html
│       └── static/cribbage/
│           ├── css/
│           ├── js/
│           └── images/
```

See:
- [steering/canon.md](steering/canon.md) — the org's facts (founding, HQ, Executive Director, motto). **Check first** when writing copy.
- [steering/content-plan.md](steering/content-plan.md) — pages, news stories, fake-org elements
- [steering/features.md](steering/features.md) — interactive features (membership form, scorer, events)
- [steering/design.md](steering/design.md) — visual direction
- [steering/tech-stack.md](steering/tech-stack.md) — Django stack details
- [steering/deployment.md](steering/deployment.md) — GitHub Actions + SSH deploy

## Quick canon (full version in steering/canon.md)

**The site is an in-universe artifact of an existing friend-group joke.** Source material
lives in `evidence/` (gitignored): emails and a WhatsApp chat with real running jokes,
characters, and lore. Mine that material before inventing anything.

Key facts:
- Founded **1893** in London; HQ "Suckling House," **The Hague**, since 1946
- Executive Director: **Patrick "Pat" Thornenberg** (also NCCWL Chairman)
- President / Champion of Champions: **Tony Cullen**
- Secretary-General / Director of Mentorship: **Alicia Lake** (Masters, founder of the
  Double Lotus Shuffle)
- Director of Digital Affairs / site author (in-universe): **Douglas Ronne** (Level 3.14)
- Motto: ***Quindecim duo*** — "fifteen, two"
- Sign-offs: *"Yours in cribbage,"* / *"Cribbage is life."*

**Narrative spine:** Tony Cullen and Alicia Lake's rise to the top of the Association followed
by their fall in the **Equine Scandal** — kicking dead horses and forcing horses (who can't
count past 3 or pronounce "31") to play sanctioned cribbage. Pat and Bart are fictional;
Tony, Alicia, and Doug are the real friends in on it.

**Constraints** (full detail in canon.md):
- **Michelle Cullen, Katrina, and Tim are off-limits for any unflattering portrayal.**
  Michelle is the long-suffering wife enduring Tony's antics with grace; Katrina is a
  respected benefactress; Tim is an earnest, competent officer.
- Do not publish real email addresses, real street addresses, or real photos without consent

## Key principles

1. **Mirror dsronne_com's stack and deploy strategy** — do not invent new infrastructure.
2. **Static-first** — content is hand-authored in templates; no CMS, no DB-backed content unless
   explicitly required later. SQLite stays the default DB for Django's own machinery only.
3. **No third-party JS frameworks** — vanilla HTML/CSS/JS, same as reference. Keep the page weight
   small enough to feel like a 2005-era association site that got a modest 2018 refresh.
4. **Commit the joke** — copy should sound like a real federation. No emoji, no "lol", no breaking
   the fourth wall. The reader should have to do a double-take.
