import pluggy
from typing import TypeAlias

Context:TypeAlias = dict[str, str]
Prompt:TypeAlias = list[str]


hookspec = pluggy.HookspecMarker("up")
hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")


