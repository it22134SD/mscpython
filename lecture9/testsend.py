from libgmail import gmailapi

subject = 'Test e-mail'
to = 'thkam@hua.gr'
body = \
"""
This is a test email
using the gmail API
"""

attachment = 'pic.png'
g = gmailapi()
g.send(to, subject, body, attachments = [attachment])
