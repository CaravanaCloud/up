from .action import *
from .command import *
from .log import *
from .fibo import up_fibo
from .action_wait import wait
from .action_install import install
from .action_template import template


def up_init():
    debug("initializing core actions")
    register_action("wait", wait)
    register_action("install", install)
    register_action("template", template)
    register_command(("fibo",), up_fibo)
