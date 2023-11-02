import pluggy
from typing import TypeAlias


Context: TypeAlias = dict[str, str]
Prompt: TypeAlias = list[str]


hookspec = pluggy.HookspecMarker("up")
hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")

from .match import does_match, match_prompt
from .containers import RunConfig

__all__ = [Context,
           Prompt,
           RunConfig,
           hookspec,
           hookimpl,
           pm,
           does_match,
           match_prompt]
