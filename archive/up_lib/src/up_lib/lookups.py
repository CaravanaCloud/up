from typing import Callable
import os

LookupHandler = Callable[[str], str]


_lookup_handlers: dict[str, LookupHandler] = {}


def register_lookup(var_name: str, handler: LookupHandler):
    _lookup_handlers[var_name] = handler


def unregister_lookup(var_name: str):
    _lookup_handlers.pop(var_name, None)


def get_lookup(var_name:str) -> LookupHandler:
    handler = _lookup_handlers.get(var_name, None)
    return handler


def lookup(var_name: str) -> str:
    value = os.environ.get(var_name, None)
    if value:
        return value
    handler = get_lookup(var_name)
    if handler:
        return handler(var_name)
    return None