import sys
import logging as log
from datetime import datetime

from up_cli import pm, containers
from .plugins import load_plugins
from .containers import *

containers = Containers()

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
    if not prompt:
        log.error("No prompts found")
        exit_cli("NO_PROMPT_FOUND")
    load_plugins(context)
    run_configs = to_run_configs(prompt)
    log.debug("run_configs: %s", run_configs)  
    for run_config in run_configs:
        containers.run(run_config)

def to_run_configs(prompt:list[str]) -> list[RunConfig]:
    result = pm.hook.to_run_configs(prompt=prompt)
    if not result:
        result = []
    return result    


if __name__ == '__main__':
    main()
