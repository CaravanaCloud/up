from .action import *
from .command import *
from .log import *
from .parser import *
#TODO Separate to split files (wait_external / wait_internal)
import subprocess
import asyncio

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
        result = wait_internal(handler, command_opts)
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
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except FileNotFoundError as e:
            debug("Command not found: %s", e)
            return {}

def wait_internal(handler, options):
    timeout = None
    if "atMost" in options:
        timeout = int(options["atMost"])
    debug(f"TODO: Internal function timeout: {timeout}")
    #TODO
    result = handler(options)
    return result
