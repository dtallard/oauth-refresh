"""
Refresh oauth2 token with `gmail.readonly` scope
"""

import os.path

import click

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]


@click.command()
@click.option("--creds_path", default="creds/credentials.json", help="Path to GCP credentials file")
@click.option("--token_path", default="creds/token.json", help="Path to GCP credentials file")
def refresh_oauth2_token(creds_path: str, token_path: str) -> None:
    """Refresh oauth2 token.

    :param creds_path: Path to credentials file generated from GCP credentials UI: https://console.cloud.google.com/apis/credentials
    :param token_path: str
    """
    creds = None

    # check if token file exists, otherwise generate one
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_path, SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    print(f"Token file refreshed at {token_path}")


if __name__ == "__main__":
    refresh_oauth2_token()
