# OAuth2 Token Refresh Script

This Python script helps you refresh your OAuth2 token for the Gmail API with the `gmail.readonly` scope.
The script is designed to handle the OAuth2 token lifecycle, ensuring you always have a valid token for accessing Gmail data.

## Requirements

Before running the script, ensure that you have the following prerequisites installed:

- Python 3.11 or higher
- Google Cloud Platform (GCP) project with the Gmail API enabled
- The `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, and `google-api-python-client` packages installed.

You can install the required dependencies by running:

```bash
pip install -r requirements/requirements.txt
```

## Setup

1. **Create a project on Google Cloud Console**:
   - Navigate to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the Gmail API by going to the "API & Services" section, then "Library", and searching for "Gmail API".
   - Go to the "Credentials" tab and create credentials for OAuth 2.0 Client IDs.

2. **Download Credentials**:
   - After creating the credentials, download the `credentials.json` file. This file will be used by the script for authentication.

3. **Place the Credentials File**:
   - Place the downloaded `credentials.json` file in the directory where you will run the script, or specify its path via the `--creds_path` option.

## Usage

### Command-line Interface (CLI)

You can run the script using the following command:

```bash
python refresh_oauth2_token.py --creds_path /path/to/credentials.json --token_path /path/to/token.json
```

#### Options:
- `--creds_path`: Path to the OAuth2 credentials file (default: `creds/credentials.json`).
- `--token_path`: Path to the OAuth2 token file (default: `creds/token.json`).

The script will check if a valid token exists at the given path (`--token_path`).
If not, or if the token has expired, it will either refresh the token (if a refresh token is available) or prompt you to authenticate via your browser.

## Flow
1. **Check for Existing Token**:
   - If a token exists at the specified `--token_path`, it will attempt to load it.
   - If the token is expired but refreshable (using a refresh token), it will refresh the token.

2. **Generate New Token**:
   - If no valid token is found, the script will prompt you to log in via your browser and will store the new token in the specified `--token_path`.

3. **Save New Token**:
   - Once refreshed or generated, the token is saved to the file at `--token_path` for future use.

## Example

```bash
python refresh_oauth2_token.py --creds_path "path/to/credentials.json" --token_path "path/to/token.json"
```

If successful, the script will output a message like:

```
Token file refreshed at path/to/token.json
```

## Notes

- If you change the `SCOPES` variable in the script (e.g., by adding new permissions), you should delete the `token.json` file to trigger re-authentication.
- The script assumes that the `credentials.json` and `token.json` files are located in the specified paths. You can adjust the paths using the `--creds_path` and `--token_path` options.
