# -*- coding: utf-8 -*-
"""Script attempts to send a message without first establishing a connection.

The fields can be left blank, as an exception SimpleEmailerError will be
raised anyway.
"""

from simple_emailer import send_email, SimpleEmailerError


try:
    send_email(
        email_text="",
        recipient_email="",
        sender_email="",
        subject=""
    )
except SimpleEmailerError as e:
    print(e)
