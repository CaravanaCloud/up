import sys
from datetime import datetime
import shlex

import uplib as up
log = up.log

def print_help():
    log.debug("up [prompt]")


def exit_cli(code=-1):
    if code:
        log.error("Exiting up cli with code %s", code)
    sys.exit(code)


def main():
    now = datetime.now()
    log.info(f"Starting UP cli at {now.isoformat()}")
    args = sys.argv
    len_args = len(args)
    if len_args < 1:
        print_help()
        exit_cli("NO_COMMAND_SPECIFIED")
    executable = args[0]
    prompt = args[1:]
    context = {"executable": executable}
    try:
        up.up_main(context, prompt)
    except Exception as e:
        log.error(e)
        exit_cli("UP_ERROR")
        
if __name__ == "__main__":
    main()
