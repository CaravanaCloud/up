from .log import *
from .parser import parse
from .wait import wait

_handlers = {
    ("wait",): wait
}


def up(prompt):
    cmd = parse(prompt)
    debug(cmd)
    command = cmd.command
    handler = _handlers.get(command)
    if handler:
        debug("Dispatching to handler")
        handler(cmd)
    else:
        debug("Handler not found for command %s", command)
    debug(f"Done up() for promopt %s", prompt)

