"""Locally grant one Gmail read-only OAuth token for independent GitHub Actions.

Run on YOUR computer. This script never uploads or commits credentials.
Do not send the produced token, credentials file or its screenshot in ChatGPT.
"""
import json
import os
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
CREDENTIALS = Path(os.environ.get("GOOGLE_OAUTH_CREDENTIALS_FILE", "credentials.json"))

if not CREDENTIALS.is_file():
    raise SystemExit("Download Desktop app OAuth credentials.json from Google Cloud into the current working directory.")

flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS), SCOPES)
credentials = flow.run_local_server(
    host="localhost", port=0, authorization_prompt_message="Open this URL in a browser: {url}",
    success_message="Fashion CRM Radar permission granted. Return to the terminal.", open_browser=True,
    access_type="offline", prompt="consent",
)
if not credentials.refresh_token:
    raise SystemExit("No refresh token granted. Check offline access and Google OAuth app status.")
print("\nAuthorization succeeded. SAVE THE NEXT VALUES ONLY in GitHub repository Secrets:")
print("GMAIL_OAUTH_CLIENT_ID:       from downloaded credentials.json")
print("GMAIL_OAUTH_CLIENT_SECRET:   from downloaded credentials.json")
print("GMAIL_OAUTH_REFRESH_TOKEN:   use the token shown below")
print("=== START REFRESH TOKEN ===")
print(credentials.refresh_token)
print("=== END REFRESH TOKEN ===")
print("\nThe refresh token is a password-like secret. Do not paste it into chat, email, or source files.")
print("Delete local credentials.json if you no longer need it; never commit it.")
