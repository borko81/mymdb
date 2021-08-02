from django.contrib import messages
from django.contrib.auth.signals import user_logged_out


def show_message(sender, user, request, **kwargs):
    messages.info(request, f'{user} have been logged out.')


user_logged_out.connect(show_message)
