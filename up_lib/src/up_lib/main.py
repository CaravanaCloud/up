from .log import *
from .parser import parse_action
from .wait import wait
from .loader import load_plugins
from .action import *


def up(context, prompt) -> dict:
    init_logging()
    debug(f"Starting up() for prompt %s", prompt)
    load_plugins()
    (action, opts, prompt) = parse_action(prompt)
    trace(f"Parsed action: %s", action)
    trace(f"Parsed action options: %s", opts)
    trace(f"Parsed action prompt: %s", prompt)
    handler = get_action(action)
    if handler:
        trace("Dispatching [%s] to handler", action)
        result = handler(opts, prompt)
        trace(f"Done up() for prompt %s with result %s", prompt, result)
        return result
    else:
        debug("Handler not found for action %s", action)
        return {}


