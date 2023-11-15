import sys
import logging
from .config import get_log_level

TRACE = 5

def init_logging():
    sys.set_int_max_str_digits(999999)    
    level = get_log_level()
    logging.basicConfig(stream=sys.stderr, level=level)
    log = logging.getLogger("up")
    return log

log = init_logging()