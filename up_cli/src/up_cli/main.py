import sys
import logging as log
import up_lib
from datetime import datetime


def print_help():
    log.debug("Please please help me")


def exit_cli(code=-1):
    if code:
        log.error("Exiting up cli with code %s", code)
    sys.exit(code)


def main():
    now = datetime.now()
    up_lib.init_logging()
    log.info(f"Starting up cli at {now.isoformat()}")
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
        up_lib.up(line= line,
                context= context)
    except Exception as ex:
        exit_cli(333)

if __name__ == '__main__':
    main()

