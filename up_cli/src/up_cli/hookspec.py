import pluggy


hookspec = pluggy.HookspecMarker("up")

RunConfigs = List[float]
Prompt = list[str]

@hookspec(firstresult=True)
def to_run_configs(prompt: Prompt) -> RunConfigs:
    """Present run configurations to execute for prompt"""

