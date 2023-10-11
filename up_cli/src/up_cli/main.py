import sys
import logging as log
from datetime import datetime

from up_cli import pm
from .plugins import load_plugins


# from up_splat import *

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
    prompt = args[1:]
    log.debug(f"executable: {executable}")
    log.debug(f"prompt: {prompt}")
    context = {
        "executable": executable
    }
    load_plugins(context)
    try:
        log.info("UP entrypoint reached")
        start_container(prompt)
        log.debug("UP done")
    except Exception as ex:
        print(ex)
        exit_cli(333)

def start_container(prompt):
    log.info("Starting container")
    log.info("PROMPT IS" + str(type(prompt)) )
    results = pm.hook.image_for_prompt(prompt=prompt)
    log.info(results)
    if len(results) > 1:
        log.warn("More than one image returned, using first")
    image = results[0] if results else None
    print(results)
    
    


if __name__ == '__main__':
    main()
