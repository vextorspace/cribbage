# Deployment

Identical pattern to `../dsronne_com/`: push to `main` → GitHub Actions runs tests → SSH into the
server → `git pull` → reinstall deps → migrate → collectstatic → restart gunicorn.

## GitHub Actions workflow

`.github/workflows/deploy.yml` — model on dsronne_com's workflow. Substitute names:

- Trigger: push to `main`
- Steps: checkout → install deps → run tests (`python cribbage/manage.py test`) → ssh-agent →
  add known_hosts → ssh deploy block
- SSH target: same server as dsronne_com (confirmed). User `vextorspace`.
- Repo checkout path on server: `~/internationalcribbageassociation.org`
- Service name: `gunicorn-cribbage` (avoid collision with dsronne's `gunicorn` service)

## Secrets needed in GitHub repo

- `SSH_DEPLAY_PRIVATE_KEY` — match dsronne_com's exact name (yes, it's misspelled there; mirror it
  unless we're standardizing across both repos)
- `SSH_KNOWN_HOST` — host key for the deploy server

## Server-side prerequisites (one-time setup, not in the workflow)

These need to happen before the first deploy succeeds:

1. Clone repo to `~/internationalcribbageassociation.org`
2. Create `.venv` and `pip install -r requirements.txt`
3. Create `.env` with `SECRET_KEY`
4. Create systemd unit `gunicorn-cribbage.service` pointing at the venv's gunicorn binary
5. Configure nginx server block for `www.internationalcribbageassociation.org` with TLS
   (Let's Encrypt via certbot, presumably same as dsronne_com)
6. DNS: `A`/`AAAA` for `internationalcribbageassociation.org` and `www.` to the server IP

Document the actual commands in `steering/server-setup.md` once we run them.

## DNS / domain

- Domain `internationalcribbageassociation.org` is registered and DNS is configured (confirmed).
- Canonical hostname: `www.internationalcribbageassociation.org`. Apex should 301-redirect to `www.`
  (handle in nginx).
- TLS via Let's Encrypt / certbot for both names.

## Coexistence with dsronne.com on the same host

Both sites share the same server. To avoid collisions:

- Separate systemd unit: `gunicorn-cribbage.service` (dsronne uses `gunicorn`)
- Separate gunicorn socket / port (e.g. dsronne on :8000, cribbage on :8001 — or unix sockets
  at `/run/gunicorn-cribbage.sock`)
- Separate nginx server block keyed on `server_name`
- Separate venv inside the cribbage repo checkout
- Separate `.env`
- Separate Let's Encrypt cert (or a combined cert covering both — certbot handles either)
