from typing import Callable

Action = Callable[[dict[str, ...], list[str]], dict]

action_handlers: dict[str, Action] = {}


def register_action(action: str, handler: Action):
    action_handlers[action] = handler


def unregister_action(action: str):
    action_handlers.pop(action, None)


def get_action(action:str) -> Action:
    try:
        handler = action_handlers.get(action)
    except KeyError:
        raise ValueError(f"Action {action} not found")
    return handler
