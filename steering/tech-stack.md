# Tech stack

Mirror `../dsronne_com/` exactly unless there's a documented reason to diverge.

## Runtime

- **Language:** Python 3 (whatever version is on the deploy host — match dsronne_com).
- **Framework:** Django 5.1.x
- **App server:** Gunicorn (run under systemd as a `gunicorn` service)
- **DB:** SQLite (only because Django needs one; site content is template-authored)
- **Reverse proxy:** Whatever fronts dsronne_com on the host (presumed nginx); reuse the same
  pattern. Confirm before writing nginx config.

## Python dependencies

Start with a minimal `requirements.txt`:

```
Django==5.1.6
gunicorn==23.0.0
python-dotenv==1.0.1
```

Do **not** pull in the langchain / openai / tavily stack from dsronne_com — those exist for the
AI librarian features on that site. The ICA site has no AI features (yet).

## Frontend

- Vanilla HTML5 + CSS3, no build step.
- Optional small vanilla JS for things like a news carousel or rules accordion.
- No React, Vue, Tailwind, or other tooling.
- Fonts: a serif headline + clean sans body. Consider Google Fonts (e.g. Playfair Display +
  Source Sans 3) — federation sites tend to favor serifs for "tradition."

## Settings file conventions (from dsronne_com)

- `SECRET_KEY` from `.env` via `python-dotenv`
- `DEBUG = False` in committed settings
- `ALLOWED_HOSTS` includes `127.0.0.1`, `localhost`, and the production domain
- `STATIC_ROOT = BASE_DIR / 'staticfiles'`
- `STATICFILES_DIRS = [BASE_DIR / 'cribbage' / 'static']`
- Single app named `cribbage` registered in `INSTALLED_APPS`
