from .up_lib import hello_world_from_lib

__version__ = '0.1.4'


def hello_world_from_init():
    return "hello world from init"


__all__ = [
    hello_world_from_lib,
    hello_world_from_init
]
