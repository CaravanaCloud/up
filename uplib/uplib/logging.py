import sys
import logging
from .config import get_log_level
from rich.logging import RichHandler

TRACE = 5

def init_logging():
    sys.set_int_max_str_digits(999999)    
    level = get_log_level()
    print("Initializing logging with level "+str(level))
    logging.basicConfig(
        level=level
    )
    #TODO: Configure rich log handler
    # https://rich.readthedocs.io/en/stable/logging.html
    log = logging.getLogger("up")
    log.setLevel(level)
    # print("Testing logging PRINT at level "+str(level))
    # log.info("Testing logging INFO at level "+str(level))
    # log.error("Testing logging ERROR at level "+str(level))
    # log.debug("Testing logging DEBUG at level "+str(level))
    # log.warning("Testing logging WARNING at level "+str(level))
    return log

log = init_logging()
