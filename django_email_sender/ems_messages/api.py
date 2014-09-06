import logging
from django_email_sender.ems_messages.utils import logged


logger = logging.getLogger(__name__)


@logged(logger)
def save_message(message):
    """
    Saves a message in database
    """
    message.save()
    return message
