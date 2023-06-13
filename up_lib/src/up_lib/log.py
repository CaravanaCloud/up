import logging
import inspect
import sys

sys.set_int_max_str_digits(999999)

def debug(*args, **kwargs):
    caller = inspect.currentframe().f_back.f_code.co_name
    logger = logging.getLogger(caller)
    logger.debug(*args, **kwargs)


def trace(*args, **kwargs):
    caller = inspect.currentframe().f_back.f_code.co_name
    logger = logging.getLogger(caller)
    logger.log(5, *args, **kwargs)
