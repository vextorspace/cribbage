# Visual design — old-money gilt

The site reads like the printed bulletin of a Victorian-era gentleman's club brought
forward to 2026: aged parchment, deep mahogany, real gilt. A first-time visitor should
feel they've found something very old and very serious.

## Reference aesthetic

- Christie's auction catalogues
- The Royal Society's publications
- Vatican stationery
- Old Pall Mall club menus
- Heirloom leather-bound book covers with gilt-foil stamping
- The British Library reading rooms
- Wax-sealed correspondence between European foreign ministries circa 1890

## Palette

| Token | Value | Use |
| --- | --- | --- |
| `--color-parchment` | `#f3e9cf` | Page background |
| `--color-parchment-alt` | `#ede0c0` | Section variant |
| `--color-surface` | `#fbf6e9` | Cards, welcome, page-header surface |
| `--color-ink` | `#261a0d` | Body text |
| `--color-ink-soft` | `#4a3520` | Muted text |
| `--color-mahogany` | `#1f1208` | Header / footer background |
| `--color-mahogany-soft` | `#2c1c11` | Crest interior |
| `--color-oxblood` | `#5a161c` | Body link color |
| `--color-forest` | `#18361c` | Headlines |
| `--color-gilt` | `#b8862e` | Gilt borders, dividers, ornaments |
| `--color-gilt-deep` | `#7a5418` | Gilt shadows |
| `--color-gilt-light` | `#e9c66a` | Gilt highlights, footer link |
| `--color-gilt-pale` | `#f4dfa0` | Hover highlight |

**The gilt gradient** (`--gilt-gradient`) is a five-stop linear gradient that simulates
the play of light across actual gold leaf — pale highlight, mid gold, deep shadow, and
back up to a secondary highlight. It's used on the hero title (via the `.gilt` utility
with `background-clip: text`), on horizontal rules, on the top/bottom borders of the
hero and the header/footer, and on the primary button fill.

## Typography

- **Display:** Cinzel — Roman inscriptional capitals, the lettering of monuments and
  museum plaques. Used for the brand name, h1, h2, h3, nav links, bulletin titles, the
  Pat sign-off block, and section headings. Letter-spaced generously (0.04–0.22em
  depending on size and context).
- **Body:** EB Garamond — humanist serif, descended from Claude Garamond's 16th-century
  cuts. Used for all body copy, page-header ledes (italic), the hero lede (italic), and
  the placeholder notes.
- **Roman numerals** are preferred for the founding year and copyright line:
  *Established MDCCCXCIII*; *MDCCCXCIII — MMXXVI*.

## Ornamental devices

- **`❦` (FLEURON)** — the house ornament. Appears as the centerpiece of section dividers
  (`.ornament` element with gilt rules on either side), at the corners of the hero text
  block, and after every `.section-heading`.
- **Double / triple gilt borders** — bulletins are framed with three nested gilt rules
  via inset box-shadows on the surface color; placeholder notes use the same technique.
- **Drop caps** — the first paragraph of the "From the Executive Director" block on the
  home page receives an oversize Cinzel drop cap rendered in the gilt gradient. Plan to
  use the same treatment on the Pat bio and rules sections.
- **Gilt top and bottom borders on hero** — 6px gilt-gradient stripes top and bottom of
  the hero section, with a 1px shadow rule for definition.

## Layout

- Centered, single-column structure (no sidebars). Max content width 1100px; narrow
  content (welcome statement, page body text) 720px.
- Sections separated by full-bleed background-color changes (parchment → surface
  cream → parchment-alt) plus a single hairline gilt rule.
- The hero is bordered top and bottom by full-width gilt-gradient bars, framing it
  like a printed announcement.

## What to avoid

- Modern startup gradients (the gilt gradient is the only one), glassmorphism, hand-drawn
  illustrations, dark-mode toggle, animation beyond simple hover transitions.
- Emoji anywhere in the UI.
- Casual microcopy ("Hey there!", "Let's get started").
- Sans-serif fonts. The whole site is set in two serifs by design.
- Bright primary colors. The palette is intentionally narrow: deep tones plus gilt.
