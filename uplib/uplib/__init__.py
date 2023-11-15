import pluggy
from typing import TypeAlias


Context: TypeAlias = dict[str, str]
Prompt: TypeAlias = list[str]


# TODO: Consider moving all globals to a single object
hookspec = pluggy.HookspecMarker("up")
hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")
settings_maps = {}

from .match import does_match, if_prompt_matches
from .containers import ContainerRun, ContainerRuns
from .main import up_main
from .logging import log


__all__ = [Context,
           Prompt,
           ContainerRun,
           ContainerRuns,
           hookspec,
           hookimpl,
           pm,
           does_match,
           if_prompt_matches,
           up_main,
           log]
