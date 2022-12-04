from libcalendar import calendarapi, google_event

c = calendarapi()
e = google_event('Test1')
c.create_event(e)

e2 = google_event('Test2', attendees = ['thkam@hua.gr'])
c.create_event(e2)
