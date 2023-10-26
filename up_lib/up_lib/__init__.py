import pluggy
from typing import TypeAlias

Context:TypeAlias = dict[str, str]
Prompt:TypeAlias = list[str]

hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")

from .match import match_prompt
from .containers import RunConfig, RunConfigs
