from .command import *
from .log import *
from .wait import wait


def up_init():
    debug("initializing core commands")
    register_command("wait", wait)
