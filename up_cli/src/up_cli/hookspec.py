import pluggy

hookspec = pluggy.HookspecMarker("up")


@hookspec
def image_for_prompt(prompt):
    """My special little hook that you can customize."""

