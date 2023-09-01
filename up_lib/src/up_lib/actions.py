from typing import Callable
from enum import Enum
from dataclasses import dataclass, astuple

from .log import *
import sys

ActionOptions = dict[str, int | str | bool]
ActionPrompt = list[str]
ActionResult = dict
ActionHandler = Callable[[ActionOptions, ActionPrompt], ActionResult]

# TODO: Consolidate global state in a single class
_action_handlers: dict[str, ActionHandler] = {}


@dataclass
class Action:
    name: str
    options: ActionOptions
    prompt: ActionPrompt

    def as_tuple(self):
        return astuple(self)




def register_action(action: str, handler: ActionHandler):
    _action_handlers[action] = handler


def unregister_action(action: str):
    _action_handlers.pop(action, None)


def get_action(action:str) -> ActionHandler:
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
    VARS_NOT_FOUND = {}

    @classmethod
    def throw(action_error, message):
        raise Exception(message) 



def print_stack_trace():
    False


def action_ok():
    debug(f"Action resulted OK")
    return {}