import pluggy
from up_lib import Prompt
from up_lib.containers import RunConfigs


@hookspec(firstresult=True)
def run_for_prompt(prompt: Prompt) -> RunConfigs:
    """Present run configurations to execute for prompt"""

