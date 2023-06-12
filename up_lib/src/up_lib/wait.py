from .command import  *
from .log import *
import shlex, subprocess


def wait (cmd: Command):
    debug("waiting %s", cmd.prompt)
    prompt = cmd.prompt
    subprocess.run(prompt)
    debug("done waiting %s", cmd.prompt)
    pass

