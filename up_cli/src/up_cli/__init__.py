import pluggy
from typing import TypeAlias

Prompt:TypeAlias = list[str]

# Is this the right way to do this?
from .containers import RunConfig
from .match import match_prompt

hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")






