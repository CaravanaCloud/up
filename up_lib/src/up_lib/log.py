import logging
import inspect
import sys
import os


def cfg_logging_level():
    level_name = os.environ.get('UP_LOG_LEVEL', 'info').lower()
    match level_name:
        case "trace": return 5
        case "debug": return logging.DEBUG
        case "info": return logging.INFO
        case "warning": return logging.WARNING
        case "error": return logging.ERROR
        case _: return logging.INFO + 1


def init_logging():
    sys.set_int_max_str_digits(999999)
    level = cfg_logging_level()
    logging.basicConfig(stream=sys.stderr, level=level)


def get_logger(name):
    logger = logging.getLogger(name)
    return logger

def error(*args, **kwargs):
    logger = get_logger(inspect.currentframe().f_back.f_code.co_name)
    logger.error(*args, **kwargs)


def warning(*args, **kwargs):
    logger = get_logger(inspect.currentframe().f_back.f_code.co_name)
    logger.warning(*args, **kwargs)


def info(*args, **kwargs):
    logger = get_logger(inspect.currentframe().f_back.f_code.co_name)
    logger.info(*args, **kwargs)


def debug(*args, **kwargs):
    logger = get_logger(inspect.currentframe().f_back.f_code.co_name)
    logger.debug(*args, **kwargs)


def trace(*args, **kwargs):
    logger = get_logger(inspect.currentframe().f_back.f_code.co_name)
    logger.log(5, *args, **kwargs)


