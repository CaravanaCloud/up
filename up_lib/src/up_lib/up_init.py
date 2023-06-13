from .action import *
from .command import *
from .log import *
from .wait import wait
from .fibo import up_fibo


def up_init():
    debug("initializing core actions")
    register_action("wait", wait)
    register_command(("fibo",), up_fibo)
