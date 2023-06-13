from .log import *
import subprocess


_wait = "wait"


def wait(opts: dict, prompt: list):
    debug("waiting %s", prompt)
    subprocess.run(prompt)
    debug("done waiting %s", prompt)
    return {}
