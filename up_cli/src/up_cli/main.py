import sys
import logging as log
from datetime import datetime

from up_cli import pm, containers
from .plugins import load_plugins
from .containers import *

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
    prompts = lookup_substituitons_for_prompt(prompt)
    for prompt in prompts:
        run_prompt(prompt)

def run_prompt(prompt:list[str]):
    try:
        log.info("UP entrypoint reached")
        start_container(prompt)
        log.debug("UP done")
    except Exception as ex:
        print(ex)
        exit_cli(333)
        
def lookup_substituitons_for_prompt(prompt):
    log.info("Looking up substitutions")
    # list[list[list[str]]]
    substs = pm.hook.substitutions_for_prompt(prompt=prompt)
    if not substs:
        log.debug("No substitutions found")
        return [prompt]
    else:
        log.debug("*** SUBSTS FOUND *** ")
        log.debug(substs)
    result = []
    for subst in substs:
        for prompt in substs:
            result.append(prompt)
    return result

def default_image():
    return "fedora:38"

def start_container(prompt):
    log.info("Starting container for prompt: %s",prompt)
    image = pm.hook.image_for_prompt(prompt=prompt)
    log.info(image)
    if not image:
        log.error("No image found for prompt: %s", prompt)
        image = default_image()
    containers.run(ContainerRun(image=image, prompt=prompt))
    log.info("Container started")

if __name__ == '__main__':
    main()
