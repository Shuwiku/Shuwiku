# -*- coding: utf-8 -*-
"""The script attempts to connect to the server with incorrect data.

Do not fill in the fields.
"""

from simple_emailer import create_connection, SimpleEmailerError


try:
    create_connection(
        sender_email="",
        sender_password=""
    )
except SimpleEmailerError as e:
    print(e)
