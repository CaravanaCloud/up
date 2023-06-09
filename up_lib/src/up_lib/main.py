from .log import *
from .parser import *


def up(prompt):
    cmd = parse(prompt)
    debug(cmd)
    debug(f"done up()")

