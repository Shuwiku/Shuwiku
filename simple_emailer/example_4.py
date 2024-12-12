# -*- coding: utf-8 -*-
"""Using a function for quick email sending.

Does not require establishing a connection beforehand.

Be sure to change the fields 'sender_email' and 'sender_password', otherwise a
SimpleEmailerError exception will be raised.
"""

from simple_emailer import send_email_quick, SimpleEmailerError


recipient_email: str = "recipient_email@example.com"
sender_email: str = "sender_email@example.com"
sender_password: str = "abcd edgh ijkl mnop"
subject: str = "Email subject."

with open("example_email.html", mode="r", encoding="utf-8") as f:
    email_text = f.read()

try:
    send_email_quick(
        email_text=email_text,
        recipient_email=recipient_email,
        sender_email=sender_email,
        sender_password=sender_password,
        subject=subject
    )
except SimpleEmailerError as e:
    print(e)
