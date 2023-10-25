import pluggy
from typing import TypeAlias

Context:TypeAlias = dict[str, str]
Prompt:TypeAlias = list[str]


# Is this the right way to do this?
from .containers import RunConfig
from .match import match_prompt

hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")






