from typing import Callable
from enum import Enum
from .log import *
import sys


Action = Callable[[dict[str, ...], list[str]], dict]

_action_handlers: dict[str, Action] = {}


def register_action(action: str, handler: Action):
    _action_handlers[action] = handler


def unregister_action(action: str):
    _action_handlers.pop(action, None)


def get_action(action:str) -> Action:
    try:
        handler = _action_handlers.get(action)
    except KeyError:
        raise ValueError(f"Action {action} not found")
    return handler


def list_action_names():
    return _action_handlers.keys()


def action_handlers():
    return _action_handlers


class ActionError(Enum):
    TIMEOUT_EXCEEDED = {}


def halt_on_error():
    # TODO: User defined configuration?
    return True


def error_of(action_error):
    return 333


def halt(action_error):
    error_code = error_of(action_error)
    sys.exit(error_code)


def print_stack_trace():
    False


def action_error(action_error, exception):
    kwargs = {}
    if print_stack_trace():
        kwargs["exc_info"] = exception
    warning(str(action_error), **kwargs)
        
    if halt_on_error():
        halt(action_error)

