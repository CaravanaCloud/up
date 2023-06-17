import logging
import inspect
import sys


def init_logging():
    sys.set_int_max_str_digits(999999)
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def get_logger(name):
    logger = logging.getLogger(name)
    return logger


def warning(*args, **kwargs):
    logger = get_logger(inspect.currentframe().f_back.f_code.co_name)
    logger.warning(*args, **kwargs)



def debug(*args, **kwargs):
    logger = get_logger(inspect.currentframe().f_back.f_code.co_name)
    logger.debug(*args, **kwargs)


def trace(*args, **kwargs):
    logger = get_logger(inspect.currentframe().f_back.f_code.co_name)
    logger.log(5, *args, **kwargs)


