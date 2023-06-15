from .action import *
from .command import *
from .log import *
from .parser import *
import subprocess


_wait = "wait"

# Inspired by Awaitility https://github.com/awaitility/awaitility/wiki/Usage
# params
# atMost



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
            kwargs = {
                "args": prompt,
                "text": True,
                "capture_output": True
            }
            if "atMost" in opts:
                kwargs["timeout"] = int(opts["atMost"])
            try:
                result = subprocess.run(**kwargs)
                debug("-- Result of subprocess command -- ")
                debug(result.stdout)
            except subprocess.TimeoutExpired as e:
                debug("Timeout expired: %s", e)
                action_error(ActionError.TIMEOUT_EXCEEDED, e)
            return result
        except FileNotFoundError as e:
            debug("Command not found: %s", e)
            return {}

