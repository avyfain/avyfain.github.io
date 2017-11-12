from functools import wraps
from time import sleep

import logging


logger = logging.getLogger(__name__)


def retry(exception_to_check, tries=5, delay=1, backoff=5):
    """Decorator layer for arguments.

    Args:
        exception_to_check (Exception or tuple(Exception...)): the exception to check. If tuple,
            we check for the first one that matches.
        tries (int): number of times to try (not retry) before giving up
        delay (int): initial delay between retries, in seconds
        backoff (int): backoff multiplier e.g. value of 2 will double the delay on each retry
    Return:
        function: a new function that retries the originally input `func`
    """
    def deco_retry(func):
        """Retry calling the decorated function using an exponential backoff.

        Args:
            func (function): function to retry
        Return:
            function: a new function that retries the originally input `func`
        """

        @wraps(func)
        def f_retry(*args, **kwargs):
            """Actual retry logic

            Args:
                args: Variable length argument list.
                kwargs: Arbitrary keyword arguments.

            Return:
                function: decorated function
            """
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return_val = func(*args, **kwargs)
                    logger.info('successful on try %s', mtries)
                    return return_val
                except exception_to_check as error:
                    logger.info("%s, Retrying in %d seconds...", str(error), mdelay)
                    sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry
