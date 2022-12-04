from libgmail import gmailapi

subject = 'Test e-mail'
to = 'thkam@hua.gr'
body = \
"""
This is a test email
using the gmail API
"""

g = gmailapi()
g.create_draft(to, subject, body)
