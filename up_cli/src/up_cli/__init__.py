import pluggy
from dataclasses import dataclass
from typing import TypeAlias
from typing import Callable

hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")

# https://docker-py.readthedocs.io/en/stable/containers.html
@dataclass
class RunConfig:
    name: str
    image: str
    command: list[str]
    environment: dict[str, str]
    ports: dict[str, str]
    auto_remove: bool = True
    network_mode: str = "host"
#    volumes: dict[str, str]

RunConfigs:TypeAlias = list[RunConfig]
Prompt:TypeAlias = list[str]

def match_prompt(prompt: Prompt, 
                 mk_run_config: Callable[[], RunConfig],
                 *args) -> list[RunConfig]:
    if not prompt:
        return None
    #TODO: implement matching
    return None


