from libcalendar import calendarapi, google_event
import datetime
c = calendarapi()

now = datetime.datetime.now()
start = now - datetime.timedelta( days = 365 )
events = c.search_between(start, end = now)
print(events)
