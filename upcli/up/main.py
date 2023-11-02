import sys
import logging as log
from datetime import datetime
import shlex

from uplib import pm, Context, Prompt
from uplib.containers import Containers, ContainerRun
from uplib.plugins import load_plugins

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
    context = {"executable": executable}
    up(context, prompt)


def up(context: Context, prompt: Prompt): 
    if not prompt:
        log.error("No prompts found")
        exit_cli("NO_PROMPT_FOUND")
    if len(prompt) == 1 and " " in prompt[0]:
        prompt = shlex.split(prompt[0])
    log.debug(f"prompt: {prompt}")
    load_plugins(context)
    container_runs = containers_for_prompt(prompt)
    if not container_runs:
        log.error("No containers found, using defaults")
        container_runs = [default_container(prompt)]
    for container in container_runs:
        containers.run(container)

def default_container(prompt):
    return ContainerRun(
        image="fedora",
        command=prompt)

def containers_for_prompt(prompt) -> list[ContainerRun]:
    from_plugins = containers_from_plugins(prompt)
    from_configs = containers_from_dynaconf(prompt)
    result = from_plugins + from_configs
    return result


def containers_from_dynaconf(prompt: list[str]) -> list[ContainerRun]:
    return []


def containers_from_plugins(prompt: list[str]) -> list[ContainerRun]:
    results = pm.hook.containers_for_prompt(prompt=prompt)
    result = sum(results, [])
    if not result:
        result = []
    return result


if __name__ == "__main__":
    main()
