from .log import *
from .parser import parse
from .wait import wait
from .loader import load_plugins
from .command import *


def up(prompt):
    debug(f"Starting up() for prompt %s", prompt)
    load_plugins()
    debug("[%s] commands loaded", len(command_handlers))
    (command, opts, prompt) = parse(prompt)
    handler = get_command(command)
    if handler:
        debug("Dispatching [%s] to handler", command)
        handler(opts, prompt)
    else:
        debug("Handler not found for command %s", command)
    debug(f"Done up() for promopt %s", prompt)

