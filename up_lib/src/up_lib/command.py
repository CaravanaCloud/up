from typing import Callable


command_handlers: dict[str, Callable[[dict, list], dict]] = {}


def register_command(command: str, handler: Callable[[dict, list], dict]):
    command_handlers[command] = handler


def unregister_command(command: str):
    command_handlers.pop(command, None)


def get_command(command:str) -> Callable[[dict, list], dict]:
    try:
        handler = command_handlers.get(command)
    except KeyError:
        raise ValueError(f"Command {command} not found")
    return handler
