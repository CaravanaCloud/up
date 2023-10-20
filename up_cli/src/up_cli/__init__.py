import pluggy
import logging as log
from dataclasses import dataclass, field
from typing import TypeAlias
from typing import Callable

hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")

# https://docker-py.readthedocs.io/en/stable/containers.html
@dataclass
class RunConfig:
    name: str = field(kw_only=True, default="")
    image: str = field(kw_only=True, default="")
    command: list[str]  = field(kw_only=True, default_factory=list)
    environment: dict[str, str]  = field(kw_only=True, default_factory=dict)
    ports: dict[str, str]  = field(kw_only=True, default_factory=dict)
    volumes: dict[str, str]  = field(kw_only=True, default_factory=dict)
    auto_remove: bool  = field(kw_only=True, default=True)
    network_mode: str  = field(kw_only=True, default="host")


RunConfigs:TypeAlias = list[RunConfig]
Prompt:TypeAlias = list[str]

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



