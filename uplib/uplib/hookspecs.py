import pluggy
from . import Prompt, hookspec
from .containers import RunConfigs


@hookspec(firstresult=True)
def run_for_prompt(prompt: Prompt) -> RunConfigs:
    """Present run configurations to execute for prompt"""
