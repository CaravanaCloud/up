import pluggy
from . import Prompt
from .containers import RunConfigs

hookspec = pluggy.HookspecMarker("up")

@hookspec(firstresult=True)
def run_for_prompt(prompt: Prompt) -> RunConfigs:
    """Present run configurations to execute for prompt"""

