# VPS setup for `internationalcribbageassociation.org`

One-time server-side and GitHub-side setup to enable GitHub-Actions-driven deploys.
The VPS already hosts `dsronne_com`, so most of the SSH and Linux fundamentals are
already in place — this checklist focuses on what's new for the cribbage repo and
what needs to coexist with dsronne_com.

## Assumptions

- The VPS hosts dsronne.com and has a working GitHub Actions deploy flow for it
- The deploy user on the VPS is `vextorspace`
- The same SSH key pair will be used (the one currently named `SSH_DEPLAY_PRIVATE_KEY`
  in dsronne_com's GitHub secrets)
- DNS for `internationalcribbageassociation.org` and `www.` is already configured
  and points at this VPS

## Phase 1 — GitHub side

### 1.1 Copy the two action secrets into the cribbage repo

GitHub Actions secrets are per-repo, so the cribbage repo needs its own copies (same
values as dsronne_com):

- [ ] In `github.com/vextorspace/cribbage` → Settings → Secrets and variables → Actions:
  - [ ] Create `SSH_DEPLAY_PRIVATE_KEY` (paste the same private key as dsronne_com's)
  - [ ] Create `SSH_KNOWN_HOST` (paste the same value)

That enables **GitHub Actions → VPS** SSH. No changes needed on the VPS for this leg —
the same public key is already in `~/.ssh/authorized_keys` for `vextorspace`.

### 1.2 Give the VPS a way to `git pull` the cribbage repo

This is the **VPS → GitHub** leg, separate from above. Two clean options:

**Option A — Per-repo deploy key (recommended for isolation).**
A GitHub deploy key is a public SSH key registered on one specific repo with read
(or write) access. The same key can't be a deploy key on two repos, so we need a new one.

- [ ] On the VPS, generate a fresh keypair just for this repo:
  ```
  ssh-keygen -t ed25519 -f ~/.ssh/cribbage_deploy -N "" -C "cribbage-deploy-key"
  ```
- [ ] Add the **public** key to the GitHub cribbage repo:
  github.com/vextorspace/cribbage → Settings → Deploy keys → Add deploy key →
  paste contents of `~/.ssh/cribbage_deploy.pub`, leave "Allow write access" unchecked
- [ ] Add a small SSH config entry on the VPS so `git pull` from this repo's clone
  uses that key. Append to `~/.ssh/config`:
  ```
  Host github-cribbage
      HostName github.com
      User git
      IdentityFile ~/.ssh/cribbage_deploy
      IdentitiesOnly yes
  ```
- [ ] When you `git clone` later, use `git@github-cribbage:vextorspace/cribbage.git`
  as the remote URL (note the `github-cribbage` host alias)

**Option B — Personal SSH key already on the VPS.**
If `vextorspace`'s VPS account already has an SSH key registered on your personal
GitHub account (so `ssh -T git@github.com` succeeds), you can just clone via
`git@github.com:vextorspace/cribbage.git` and skip the deploy-key dance.

- [ ] Test: `ssh -T git@github.com` from the VPS. If it says "Hi vextorspace! You've
      successfully authenticated…" → Option B works, skip 1.2's deploy-key steps

## Phase 2 — VPS side

All commands run as `vextorspace` unless noted.

### 2.1 Clone the repo

- [ ] `cd ~`
- [ ] `git clone <REMOTE-URL> internationalcribbageassociation.org`
      (substitute the appropriate URL from 1.2)
- [ ] `cd internationalcribbageassociation.org`

### 2.2 Python environment

- [ ] `python3 -m venv .venv`
- [ ] `source .venv/bin/activate`
- [ ] `pip install --upgrade pip`
- [ ] `pip install -r requirements.txt`
      (will fail if the project hasn't been scaffolded yet — that's fine; come back)

### 2.3 Application secrets

- [ ] Create `.env` in the repo root:
  ```
  SECRET_KEY=<generate-a-50-char-random-string>
  ```
  (Use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
  inside the venv to generate one)
- [ ] `chmod 600 .env`

### 2.4 Systemd unit for gunicorn

We need a separate service from dsronne_com's. Filename: `/etc/systemd/system/gunicorn-cribbage.service`

- [ ] Check first what dsronne_com's gunicorn binds to:
      `sudo systemctl cat gunicorn` (or whatever the unit is named) →
      note whether it uses a Unix socket or a TCP port
- [ ] Create the cribbage unit with a **different** socket/port. Recommended (Unix sockets,
      cleaner than ports):
  ```
  [Unit]
  Description=gunicorn daemon for internationalcribbageassociation.org
  After=network.target

  [Service]
  User=vextorspace
  Group=www-data
  WorkingDirectory=/home/vextorspace/internationalcribbageassociation.org/cribbage
  EnvironmentFile=/home/vextorspace/internationalcribbageassociation.org/.env
  ExecStart=/home/vextorspace/internationalcribbageassociation.org/.venv/bin/gunicorn \
            --workers 3 \
            --bind unix:/run/gunicorn-cribbage.sock \
            cribbage.wsgi:application

  [Install]
  WantedBy=multi-user.target
  ```
  (Adjust paths if the Django project layout differs.)
- [ ] `sudo systemctl daemon-reload`
- [ ] `sudo systemctl enable gunicorn-cribbage`
- [ ] (Don't start it yet — the Django code doesn't exist on disk in a runnable form
      until the first commit is deployed.)

### 2.5 Nginx vhost

- [ ] Create `/etc/nginx/sites-available/internationalcribbageassociation.org`:
  ```
  server {
      listen 80;
      server_name internationalcribbageassociation.org www.internationalcribbageassociation.org;

      location /static/ {
          alias /home/vextorspace/internationalcribbageassociation.org/cribbage/staticfiles/;
      }

      location / {
          include proxy_params;
          proxy_pass http://unix:/run/gunicorn-cribbage.sock;
      }
  }
  ```
- [ ] Symlink to enable:
      `sudo ln -s /etc/nginx/sites-available/internationalcribbageassociation.org /etc/nginx/sites-enabled/`
- [ ] `sudo nginx -t` (syntax check)
- [ ] `sudo systemctl reload nginx`

### 2.6 TLS via certbot

- [ ] `sudo certbot --nginx -d internationalcribbageassociation.org -d www.internationalcribbageassociation.org`
      (certbot will edit the nginx vhost to add the SSL block and an HTTP→HTTPS redirect)
- [ ] Test renewal:
      `sudo certbot renew --dry-run`

### 2.7 Apex → www canonical redirect

The user asked for `www.` as canonical. Certbot's default config serves both. After
certbot has done its edits, add this server block to the cribbage vhost (or let certbot's
edited file keep both `server_name`s):

```
server {
    listen 443 ssl;
    server_name internationalcribbageassociation.org;
    return 301 https://www.internationalcribbageassociation.org$request_uri;
    # SSL config lines that certbot inserted
}
```

- [ ] Edit nginx vhost so the apex 443 block 301-redirects to `www.`
- [ ] `sudo nginx -t && sudo systemctl reload nginx`

## Phase 3 — First deploy

The GitHub Actions workflow (`.github/workflows/deploy.yml`, modeled on dsronne_com's)
runs on push to main. The first time it runs:

- [ ] Confirm the workflow exists and points at the right paths (cribbage's `manage.py`,
      the right server path `~/internationalcribbageassociation.org`, the service name
      `gunicorn-cribbage`)
- [ ] Push to main and watch the Actions tab
- [ ] On the VPS, after the action succeeds:
      `sudo systemctl start gunicorn-cribbage`
      (subsequent deploys will use `restart`)
- [ ] `curl -I https://www.internationalcribbageassociation.org` → expect 200

## Phase 4 — Verify and harden

- [ ] Confirm both vhosts coexist: `curl -I https://dsronne.com` and the cribbage URL,
      both should return 200
- [ ] Check the gunicorn-cribbage logs: `sudo journalctl -u gunicorn-cribbage -f`
- [ ] Confirm static files load (the styled home page should render)
- [ ] Confirm the certbot timer is enabled:
      `sudo systemctl status certbot.timer` (or `snap services` if certbot is a snap)

## Common gotchas

- **Permissions on the socket:** if nginx can't connect to `/run/gunicorn-cribbage.sock`,
  it's usually because gunicorn's group needs to be `www-data` (set in the unit file above)
- **STATIC files 404 after first deploy:** the workflow runs `collectstatic`, but nginx
  needs to be able to read `staticfiles/`. The path in the nginx vhost must match
  exactly where `STATIC_ROOT` collects to.
- **DEBUG=True accidentally on prod:** double-check `settings.py` and that `.env` doesn't
  define `DEBUG=True`.
- **Allowed hosts:** ensure `ALLOWED_HOSTS` includes both the apex and `www.` names plus
  `127.0.0.1` and `localhost`.
- **Workflow vs. existing dsronne deploy:** the two GitHub Action workflows run independently
  and SSH in as the same user — they shouldn't conflict, but if both push at the same time
  there could be brief races in apt/systemd. Not a real problem in practice.
