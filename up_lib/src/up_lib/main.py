from .log import *
from .parser import parse
from .wait import wait
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


def up(prompt):
    debug(f"Starting up() for prompt %s", prompt)
    register_command("wait", wait)
    cmd = parse(prompt)
    debug(cmd)
    (command, options, prompt) = cmd.to_tuple()
    handler = get_command(command)
    if handler:
        debug("Dispatching [%s] to handler", command)
        handler(cmd.options, cmd.prompt)
    else:
        debug("Handler not found for command %s", command)
    debug(f"Done up() for promopt %s", prompt)

