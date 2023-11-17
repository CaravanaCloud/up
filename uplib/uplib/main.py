import shlex

from . import pm, Context, Prompt
from .containers import Containers, ContainerRun
from .plugins import load_plugins
from .logging import log
from .config import Config


def up_main(context: Context, prompt: Prompt):
    log.info("*** %s", Config.welcome_message.get() + " ***")
    containers = Containers()
    if not prompt:
        log.error("No prompts found")
        raise Exception("No prompts found")
    if len(prompt) == 1 and " " in prompt[0]:
        prompt = shlex.split(prompt[0])
    log.debug(f"prompt: {prompt}")
    load_plugins(context)
    container_runs = containers_for_prompt(prompt)
    if not container_runs:
        log.error("No containers found, using defaults")
        container_runs = [default_container(prompt)]
    for container_run in container_runs:
        containers.run(container_run)


def default_container(prompt):
    return ContainerRun(
        image=Config.default_image.get(),
        command=prompt)


def containers_for_prompt(prompt) -> list[ContainerRun]:
    from_plugins = containers_from_plugins(prompt)
    return from_plugins

def containers_from_plugins(prompt: list[str]) -> list[ContainerRun]:
    result = pm.hook.containers_for_prompt(prompt=prompt)
    if not result:
        return []
    return result
