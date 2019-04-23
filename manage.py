#!/usr/bin/env python
import os
import sys
from django.conf import settings
from django.core.mail import send_mail

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alogo.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)


subject = 'Some subject'
from_email = settings.DEFAULT_FROM_EMAIL
message = 'This is my test message'
recipient_list = ['dev@alogotech.com', 'umarsamiya@gmail.com']
html_message = '<h1>This is my HTML test</h1>'


send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)