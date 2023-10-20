import pluggy
from up_cli import Prompt, RunConfigs

hookspec = pluggy.HookspecMarker("up")

@hookspec(firstresult=True)
def run_for_prompt(prompt: Prompt) -> RunConfigs:
    """Present run configurations to execute for prompt"""

