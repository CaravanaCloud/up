import uplib as up


def create_containers(prompt):
    result = up.ContainerRun(
        image="fedora",
        command=['echo', 'LETS DEMO '] + prompt)
    return result

@up.hookimpl
def containers_for_prompt(prompt):
    return up.if_prompt_matches(create_containers, prompt, "demo")

