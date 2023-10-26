import sys
import logging as log
from datetime import datetime
import shlex

from up_lib import Context, Prompt, RunConfig
from up_lib.containers import Containers
from up_lib.plugins import load_plugins

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
    run_configs = run_configs_for_prompt(prompt)
    log.debug("run_configs: %s", run_configs)
    for run_config in run_configs:
        containers.run(run_config)


def run_configs_for_prompt(prompt) -> list[RunConfig]:
    from_plugins = run_configs_from_plugins(prompt)
    from_configs = run_configs_from_dynaconf(prompt)
    result = from_plugins + from_configs
    return result


def run_configs_from_dynaconf(prompt: list[str]) -> list[RunConfig]:
    return []


def run_configs_from_plugins(prompt: list[str]) -> list[RunConfig]:
    result = pm.hook.run_for_prompt(prompt=prompt)
    if not result:
        result = []
    return result


if __name__ == "__main__":
    main()
