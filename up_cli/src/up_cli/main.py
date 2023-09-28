import sys
import logging as log
from datetime import datetime


def print_help():
    log.debug("Please please help me")

def exit_cli(code=-1):
    if code:
        log.error("Exiting up cli with code %s", code)
    sys.exit(code)

def init():
    sys.set_int_max_str_digits(999999)
    level = log.DEBUG
    log.basicConfig(stream=sys.stderr, level=level)

def main():
    init()
    now = datetime.now()
    log.info(f"Starting UP cli at {now.isoformat()}")
    args = sys.argv
    len_args = len(args)
    if len_args < 1:
        print_help()
        exit_cli("NO_COMMAND_SPECIFIED")
    executable = args[0]
    line = args[1:]
    log.debug(f"executable: {executable}")
    log.debug(f"line: {line}")
    context = {
        "executable": executable
    }
    try:
        log.info("UP entrypoint reached")
        start_container()
        log.debug("UP done")
    except Exception as ex:
        exit_cli(333)

def start_container():
    log.info("Starting container")
    image = "caravanacloud/up_rh"
    

if __name__ == '__main__':
    main()

