from .command import *
from .log import *
from .parser import *
import subprocess


_wait = "wait"


def wait(opts: dict, prompt: list[str]):
    debug("waiting %s with %s options", prompt, len(opts))
    if len(prompt) < 1:
        return {}
    (command, command_opts) = parse_command(prompt)
    handler = get_command(command)
    if handler is not None:
        debug("Found internal command handler for %s", command)
        result = handler(command_opts)
        debug("Result of internal command")
        debug(result)
        return result
    else:
        debug("Running subprocess command %s", command)
        try:
            result = subprocess.run(prompt, text=True, capture_output=True)
            trace("Result of subprocess command")
            trace(result)
            return result
        except FileNotFoundError as e:
            debug("Command not found: %s", e)
            return {}

