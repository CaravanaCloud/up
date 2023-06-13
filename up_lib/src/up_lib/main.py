from .log import *
from .parser import parse_action
from .wait import wait
from .loader import load_plugins
from .action import *


def up(prompt):
    debug(f"Starting up() for prompt %s", prompt)
    load_plugins()
    (action, opts, prompt) = parse_action(prompt)
    debug(f"Parsed action: %s", action)
    debug(f"Parsed action options: %s", opts)
    debug(f"Parsed action prompt: %s", prompt)
    handler = get_action(action)
    if handler:
        debug("Dispatching [%s] to handler", action)
        handler(opts, prompt)
    else:
        debug("Handler not found for action %s", action)
    debug(f"Done up() for promopt %s", prompt)

