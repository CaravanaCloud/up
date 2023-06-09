from .log import *
from .parser import *


def up(prompt):
    debug(f"up I {type(prompt)} {prompt}")
    cmd = parse(prompt)
    debug(cmd)
    debug(f"done up()")
