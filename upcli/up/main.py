import sys
from datetime import datetime
import shlex
import pkgutil

import uplib

log = uplib.log

def print_help():
    log.debug("up [prompt]")

def get_modules():
    up_plugins = []
    for pkg in pkgutil.iter_modules():
        if pkg.name.startswith("up_"):
            up_plugins.append(pkg.name)
    return up_plugins

def exit_cli(code=-1):
    if code:
        log.error("Exiting up cli with code %s", code)
        if code == "NO_COMMAND_SPECIFIED":
            log.error(f"installed plugins:\n{'\n'.join(get_modules())}")
    sys.exit(code)

def cli_main():
    now = datetime.now()
    log.info(f"Starting UP cli at {now.isoformat()}")
    args = sys.argv
    len_args = len(args)
    if len_args <= 1:
        print_help()
        exit_cli("NO_COMMAND_SPECIFIED")
    executable = args[0]
    prompt = args[1:]
    context = {"executable": executable}
    try:
        uplib.up_main(context, prompt)
    except Exception as e:
        log.error(e)
        # print stack trace
        raise e
        exit_cli("UP_ERROR")
        
