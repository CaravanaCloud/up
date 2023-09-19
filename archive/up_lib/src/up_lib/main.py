from .log import *
from .parser import parse_action
from .loader import load_plugins
from .actions import *

import json

def up(line = None, context:dict = {}) -> dict:
    up_initialize()
    debug(f"up input [%s]:%s", len(line), line[0:20])
    actions = list_action_names()
    debug(f"[{len(actions)}] Action Handlers loaded")
    action = parse_action(line = line, actions = actions)
    if action:
        trace(f"Selected action: %s", str(action))
        try:
            return handle_action(action)
        except Exception as ex:
            error("Action %s failed", str(action))
            warning(ex)
            raise ex
    else:
        warning(f"No action parsed.")

def handle_action(action:Action) -> dict:
    (action_name, opts, prompt) = action.as_tuple()
    handler = get_action(action_name)
    if handler:
        trace("Dispatching [%s] to handler", action_name)
        result = handler(opts, prompt)
        trace(f"Done up() for action %s with result %s", action, result)
        output_result(result)
        return result
    else:
        debug("Handler not found for action %s", action)
        return {}


def output_result(result):
    dump = json.dumps(result, indent=2)
    print(dump)
    
def up_initialize():
    trace("Initializing up")
    init_logging()
    load_plugins()
    trace(f"Registered {list_action_names()} action handlers.")
