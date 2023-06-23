from .actions import *
from .commands import *
from .log import *
from .cmd.fibo import up_fibo
from .action.wait import wait
from .action.install import install
from .action.template import template
from .action.vars import vars


def up_init():
    debug("initializing up_lib actions")
    register_action("wait", wait)
    register_action("install", install)
    register_action("template", template)
    register_action("vars", vars)
    debug("initializing up_lib commands")
    register_command(("fibo",), up_fibo)
    debug("initializing up_lib lookups")
    register_command(("fibo",), up_fibo)
