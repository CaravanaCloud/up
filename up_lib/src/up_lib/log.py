import logging
import inspect


def debug(*args, **kwargs):
    caller = inspect.currentframe().f_back.f_code.co_name
    logger = logging.getLogger(caller)
    logger.debug(*args, **kwargs)
