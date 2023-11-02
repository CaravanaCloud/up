from . import hookspec, Prompt, ContainerRuns


@hookspec(firstresult=True)
def containers_for_prompt(prompt: Prompt) -> ContainerRuns:
    """Present run configurations to execute for prompt"""
