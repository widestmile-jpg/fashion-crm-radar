# Fashion CRM Radar

Weekly competitive email marketing research. The public GitHub Pages site contains only deliberately published editorial material.

## Subscription-independent control

The GitHub repository and its Actions workflows can be used from the **Actions** tab without a ChatGPT plugin. This is a manual-review mode, not yet a production automated email-ingestion system.

### Screenshot test (safe)

1. Open **Actions → Fashion CRM Radar — test screenshot (no publishing)**.
2. Select **Run workflow**.
3. Download **fashion-radar-screenshot-smoke-test** from the completed run.

The test generates a full-page PNG of an **anonymized reconstruction already present in this public repository**. It does **not** access Gmail, render the original email, deliver mail, or change the published report.

### Publish an explicitly approved HTML issue

1. Review the candidate report located under `issues/` before publishing.
2. Open **Actions → Fashion CRM Radar — publish approved issue → Run workflow**.
3. Enter an exact `issue_path`, e.g. `issues/2026-10-29-final-review.html`.
4. Enter `PUBLISH_APPROVED` in the confirmation field.
5. Confirm the action run succeeded and verify the public site.

This operation **replaces `index.html`**. It does not send email and it does not create a draft. Do not run it until the report is genuinely approved. There is no schedule attached to this publication workflow.

## Production work not yet done

- **Gmail access:** configure OAuth for a dedicated, minimal-scope mailbox integration (or a dedicated forwarded-mailbox), with refresh-token rotation and secure secrets outside public Git. ChatGPT's Gmail plugin is *not* a durable credential for GitHub Actions.
- **Original rendering:** obtain actual HTML MIME parts and embedded/remote resources of opted-in competitor newsletters, sanitize potentially identifying tracking pixels and links, and test rendering with Playwright.
- **Privacy:** never commit raw emails, individual links, Gmail IDs, authorization tokens or private screenshots to this **public** repository. Public GitHub Actions artifacts and Pages should be treated as shareable. Store sensitive staging data in a separate private repository or suitably access-controlled storage.
- **Research:** de-duplicate by stable message identity, preserve campaign provenance, compare brands, and produce evidence-backed findings.
- **Private review:** create a draft for explicit approval *without deploying it to public Pages*; do not assume an unlisted public URL is private.
- **Email delivery:** connect a separate authorized sender and recipients; only send after explicit approval and guard against repeated delivery.
- **Scheduling:** schedule draft preparation only after the preceding components pass end-to-end tests. Do not automatically publish or email.

## Current safety status

The external ChatGPT Fashion CRM Radar scheduled task is paused. This repository has **no automated newsletter delivery**. The publishing workflow requires an explicit confirmation in GitHub Actions.

## Next step: direct Gmail authorization (without ChatGPT plugins)

Gmail is **not connected** to this GitHub project yet. The workflow `.github/workflows/gmail-connection-check.yml` is manually runnable and only verifies read-only authorization; it never downloads or logs email content.

1. Open [Google Cloud Console](https://console.cloud.google.com/). Create or select your own project and enable **Gmail API**.
2. Configure **Google Auth platform → Branding / Audience / Data Access**. For a personal Gmail account choose **External**. In testing mode add your own account under **Test users**. Request the minimum `https://www.googleapis.com/auth/gmail.readonly` scope. This scope is considered restricted; read Google's data handling and verification rules.
3. In **Google Auth platform → Clients**, create OAuth client ID of type **Desktop app**, download the JSON as `credentials.json` **to your own computer**. Never upload this file to GitHub or ChatGPT.
4. In a local terminal with Python installed run `python -m pip install google-auth-oauthlib` and then `python scripts/google_oauth_local.py` from your own checkout of this repository. Sign in via the browser on your own device and grant **read-only** access.
5. Copy the client ID, client secret and refresh token **locally** into repository **Settings → Secrets and variables → Actions → New repository secret** as `GMAIL_OAUTH_CLIENT_ID`, `GMAIL_OAUTH_CLIENT_SECRET`, `GMAIL_OAUTH_REFRESH_TOKEN`. Do not paste them into chat.
6. Run **Actions → Fashion CRM Radar — Gmail connection check (no content) → Run workflow**. A success only confirms permission; it does not mean competitor newsletter collection works yet.

**Important longevity caveat:** for an External OAuth app in Google's **Testing** status, refresh tokens involving Gmail access generally expire after **7 days**. Long-running weekly jobs need a suitable OAuth app publishing status and compliance with applicable Google verification rules. Do not assume that a testing token enables perpetual automation.

**Public repository privacy:** this repository is currently public. Store no original Gmail HTML, private Gmail links, customer data or raw screenshots here or in GitHub Pages. Before implementing Gmail collection/rendering, set up a separate private staging repository or access-controlled storage. This connection check only retrieves up to five message IDs in memory (not content) and does not display or store any of them. GitHub Secrets protect credentials at rest, but people with write access to workflows can potentially use them.

Official references:
- https://developers.google.com/workspace/gmail/api/quickstart/python
- https://developers.google.com/workspace/gmail/api/auth/scopes
- https://developers.google.com/identity/protocols/oauth2
- https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets

