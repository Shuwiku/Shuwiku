# -*- coding: utf-8 -*-
"""An example of common usage of simple_emailer.

Be sure to change the fields 'sender_email' and 'sender_password', otherwise a
SimpleEmailerError exception will be raised.
"""

from simple_emailer import close_connection, create_connection, send_email


recipient_email: str = "recipient_email@example.com"
sender_email: str = "sender_email@example.com"
sender_password: str = "abcd edgh ijkl mnop"
subject: str = "Email subject."

with open("example_email.html", mode="r", encoding="utf-8") as f:
    email_text = f.read()

create_connection(
    sender_email=sender_email,
    sender_password=sender_password
)
send_email(
    email_text=email_text,
    recipient_email=recipient_email,
    sender_email=sender_email,
    subject=subject
)
close_connection()

print("Email sent.")
