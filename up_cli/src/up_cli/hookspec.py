import pluggy

hookspec = pluggy.HookspecMarker("up")


@hookspec(firstresult=True)
def image_for_prompt(prompt: list[str]) -> str:
    """Present the image in which the prompt will be executed"""

@hookspec(firstresult=True)
def substitutions_for_prompt(prompt: list[str]) -> list[list[str]]:
    """Present the substitutions for the prompt"""
    
# TODO: Variables and Volumes