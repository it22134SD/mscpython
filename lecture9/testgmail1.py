#---import
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# API scope
SCOPES = ['https://mail.google.com/']
creds = None
#---creds1
# Do we already have a token?
if os.path.exists('token.json'):
    # If so get credentials from token file
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# Now check whether we need to refresh the token or obtain a new one
if not creds or not creds.valid:

    # If the token has expired, refresh it
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # otherwise we must login
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

    # Save the token for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
#---creds3
try:
    # Call the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

except HttpError as error:
    print(f'An error occurred: {error}')
#---creds4
