from .actions import *
from .commands import *
from .log import *
from .cmd.fibo import up_fibo
from .action.wait import wait
from .action.install import install
from .action.template import template


def up_init():
    debug("initializing core actions")
    register_action("wait", wait)
    register_action("install", install)
    register_action("template", template)
    register_command(("fibo",), up_fibo)
