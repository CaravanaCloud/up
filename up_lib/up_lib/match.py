import logging as log
from . import Prompt
from typing import Callable
from .containers import RunConfig

def does_match(prompt: Prompt, args) -> bool:
    for p, a in zip(prompt, args):
        if p != a:
            return False
    return True

def match_prompt(mk_run_config: Callable[[], RunConfig],
                 prompt: Prompt, 
                 *args) -> list[RunConfig]:
    if not prompt:
        return None
    if does_match(prompt, args):
        log.info(f"MATCH: prompt={prompt}, args={args}")
        return [mk_run_config(prompt)]
    log.info(f"NO MATCH: prompt={prompt}, args={args}")
    return None