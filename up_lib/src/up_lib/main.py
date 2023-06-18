from .log import *
from .parser import parse_action
from .loader import load_plugins
from .action import *

import json

def up(line = None, context:dict = {}) -> dict:
    up_initialize()    
    debug(f"Processing line %s", line)
    actions = list_action_names()
    (action, opts, prompt) = parse_action(line = line, actions = actions)
    debug(f"[{len(actions)}] Actions loaded")
    debug(f"Parsed action: %s", action)
    debug(f"Parsed action options: %s", opts)
    debug(f"Parsed action prompt: %s", prompt)
    handler = get_action(action)
    if handler:
        trace("Dispatching [%s] to handler", action)
        result = handler(opts, prompt)
        trace(f"Done up() for line %s with result %s", line, result)
        output_result(result)
        return result
    else:
        debug("Handler not found for action %s", action)
        return {}

def output_result(result):
    dump = json.dumps(result, indent=2)
    print(dump)
    
def up_initialize():
    debug("*** Initializing up_cli")
    init_logging()
    load_plugins()
    debug(f"Registered action handlers {list_action_names()}")
