from typing import Callable

Command = Callable[[dict], dict]


command_handlers: dict[tuple, Command] = {}


def register_command(command: tuple, handler: Command):
    command_handlers[command] = handler


def unregister_command(command: tuple):
    command_handlers.pop(command, None)


def get_command(command:tuple) -> Command:
    handler = command_handlers.get(command, None)
    return handler
