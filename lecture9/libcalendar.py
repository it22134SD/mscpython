import os
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']
DEFAULT_ZONE = 'Europe/Athens'
DEFAULT_STAMP = '+02:00'
class google_event:
    def __init__(self, summary, location = None, description = None, time_zone = DEFAULT_ZONE,
                       start = None, end = None, attendees = []):

        if start is None:
            start = datetime.datetime.now()

        if end is None:
            end = start + datetime.timedelta(hours = 1)

        attendees_dict = [ {'email' : email} for email in attendees ]
        self.event = {
          'summary': summary,
          'location': location,
          'description': description,
          'start': {
            'dateTime': start.isoformat(),
            'timeZone': time_zone,
          },
          'end': {
            'dateTime': end.isoformat(),
            'timeZone': time_zone,
          },
          'attendees': attendees_dict
        }

    def __str__(self):
        return str(self.event)

    def __repr__(self):
        return str(self.event)


class calendarapi:

    def __init__(self, token_file = 'cal_token.json', creds_file = 'calendar_creds.json',
                 calendar_id = 'primary', time_zone = 'Europe/Athens'):


        self.calendar_id = calendar_id
        self.time_zone = time_zone
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    creds_file, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_file, 'w') as token:
                token.write(creds.to_json())

        try:
            self.service = build('calendar', 'v3', credentials=creds)

        except HttpError as error:
            print('An error occurred: %s' % error)

    def create_event(self, gevent):
        return self.service.events().insert(calendarId = self.calendar_id, body = gevent.event ).execute()

    def get_event(self, event_id):
        return self.service.events().get(calendarId = self.calendar_id, eventId = event_id ).execute()

    def search_between(self, start, end = None, max_results = 10):
        time_min = start.isoformat() + DEFAULT_STAMP
        if end is not None:
            time_max = end.isoformat() + DEFAULT_STAMP
        else:
            time_max = None
        print(time_min)
        print(time_max)
        events_result = self.service.events().list(calendarId = self.calendar_id,
                                                   timeMin = time_min,
                                                   singleEvents = True,
                                                   maxResults = max_results,
                                                   timeZone = self.time_zone,
                                                   timeMax = time_max,
                                                   orderBy = 'startTime').execute()
        events = events_result.get('items', [])
        return events
