#---import
import mimetypes
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.message import EmailMessage

SCOPES = ['https://mail.google.com/']
#---scope
class gmailapi:

    def __init__(self, token_file = 'token.json', credentials_file = 'credentials.json', from_ad = 'thomaskamalakis@gmail.com'):
        self.from_ad = from_ad
        try:
            creds = None
            if os.path.exists(token_file):
                creds = Credentials.from_authorized_user_file(token_file, SCOPES)

            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_file, SCOPES)
                    creds = flow.run_local_server(port = 0)
                with open(token_file, 'w') as token:
                    token.write(creds.to_json())

            self.service = build('gmail', 'v1', credentials = creds)

        except HttpError as error:
            print(f'An error occurred: {error}')
#---init
    def build_message(self, to, subject, body):
        message = EmailMessage()

        message['To'] = to
        message['From'] = self.from_ad
        message['Subject'] = subject
        message.set_content( body )
        return message
#---buildmessage
    def build_draft(self, message):
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {
            'message': {
                'raw': encoded_message
            }
        }
        draft = self.service.users().drafts().create(userId = "me",
                                                body = create_message).execute()
        return draft
#---builddraft
    def create_draft(self, to, subject, body):
        message = self.build_message(to, subject, body)
        return self.build_draft(message)

    def create_draft_with_attachments(self, to, subject, body, attachments = []):
        message = self.build_message(to, subject, body)

        for attachment in attachments:
            type_subtype, _ = mimetypes.guess_type(attachment)
            maintype, subtype = type_subtype.split('/')

            with open(attachment, 'rb') as f:
                data = f.read()
                filename = os.path.basename( attachment )
            message.add_attachment(data, maintype, subtype, filename = filename)
        return self.build_draft( message )
#---createdraft
    def send(self, to, subject, body, attachments = []):
        draft_dict = self.create_draft_with_attachments(to, subject, body, attachments = attachments)
        id = draft_dict['id']
        draft = self.service.users().drafts().send(body = {'id': id}, userId = 'me').execute()
#---send
