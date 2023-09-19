from ..log import *
from ..actions import *
from ..lookups import *
import os

def vars(opts: dict, prompt: list[str]) -> dict:
    debug("vars action %s with %s options", prompt, len(opts))
    unset = []
    for item in prompt:
        is_set = item in os.environ
        if not is_set:
            unset.append(item)
    if len(unset):
        raise ActionError.VARS_NOT_FOUND.throw(f"Variables not found. {unset}")
    return action_ok()
