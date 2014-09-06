import logging
from decorator import decorator


logger = logging.getLogger(__name__)


def logged(the_logger):
    """
    Protects a view if given product is not activated
    """
    @decorator
    def internal_decorator(func, *args, **kwargs):
        the_logger.debug('Calling function {} with parameters {} {}'.format(func, args, kwargs))
        result = func(*args, **kwargs)
        the_logger.debug('Function result: {}'.format(result))
        return result

    return internal_decorator


@logged(logger)
def save_message(message):
    """
    Saves a message in database
    """
    message.save()
    return message
