import pluggy
from dataclasses import dataclass
from typing import List

hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")

def match_prompt(prompt, head, image):
    if not prompt:
        return None
    if prompt[0] == head:
        return image
    return None

# https://docker-py.readthedocs.io/en/stable/containers.html
@dataclass
class RunConfig:
    name: str
    image: str
    command: List[str]
    environment: dict[str, str]
    ports: dict[str, str]
    auto_remove: bool = True
    network_mode: str = "host"
#    volumes: dict[str, str]
