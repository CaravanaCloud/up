import pluggy

hookspec = pluggy.HookspecMarker("up")


@hookspec(firstresult=True)
def image_for_prompt(prompt):
    """Present the image in which the prompt will be executed"""

