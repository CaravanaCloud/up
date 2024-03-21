import shlex
import os

from . import pm, Context, Prompt
from .containers import Containers, ContainerRun
from .plugins import load_plugins
from .logging import log
from .config import Config
from .parser import parse_doclets

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
    log.warning("==> DEBUG (%s) :\n %s", str(type(container_runs)), container_runs)
    for container_run in container_runs:
        containers.run(container_run)


def default_container(prompt):
    return ContainerRun(
        image=Config.default_image.get(),
        working_dir="/tmp/up_cwd",
        command=prompt)

def is_exec(exec: str) -> bool:
    file_exists = os.path.exists(exec)
    is_exec = os.access(exec, os.X_OK)
    result = file_exists and is_exec
    return result

def is_text_file(file_path, threshold=0.30):
    """
    Checks if the given file is a text file.
    
    Args:
    - file_path: Path to the file to be checked.
    - threshold: The fraction of non-text characters at which a file is considered binary.
    
    Returns:
    - True if the file is likely a text file, False otherwise.
    """
    text_characters = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
    is_binary = lambda bytes: bool(bytes.translate(None, text_characters))
    
    with open(file_path, 'rb') as file:
        # Read up to 1024 bytes from the file
        block = file.read(1024)
        if not block:
            # Empty file are considered text files
            return True
        if is_binary(block):
            return False
    
    # Check the proportion of binary content in the block
    num_binary = sum(is_binary(bytearray([b])) for b in block)
    if num_binary / 1024 > threshold:
        return False
    
    return True


def containers_for_prompt(prompt: list[str]) -> list[ContainerRun]:
    result = []
    if (len(prompt) == 0):
        return result
    head = prompt[0]
    if (is_exec(head)):
        result= containers_from_exec(prompt)
    else:
        lists = containers_from_plugins(prompt)
        result = [item for sublist in lists for item in sublist]
    return result

def containers_from_plugins(prompt: list[str]) -> list[ContainerRun]:
    result = pm.hook.containers_for_prompt(prompt=prompt)
    if not result:
        return []
    return result

def containers_from_exec(prompt: list[str]) -> list[ContainerRun]:
    result = []
    head = prompt[0]
    if (is_text_file(head)):
        # log.error("CONTAINERS FROM TEXT "+str(prompt))
        doclets = parse_doclets(head)
        # log.error(str(doclets))
        run = ContainerRun()
        run.command =  prompt
        run.working_dir = "/tmp/up_cwd/"
        # iterate on doclets and set the run properties
        for key in doclets:
            if key == "FROM":
                run.image = doclets[key]
            if key == "CMD":
                run.command = doclets[key]
            if key == "WORKDIR":
                run.working_dir = doclets[key]
            if key == "ENV":
                run.environment = doclets[key]
            if key == "VOLUME":
                run.volumes = doclets[key]
            if key == "PORT":
                run.ports = doclets[key]
            if key == "USER":
                run.user = doclets[key]
            if key == "ENTRYPOINT":
                run.command = doclets[key]
            
        result = [run]
    return result