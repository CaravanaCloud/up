import uplib as up

def run_container(prompt):
    return up.ContainerRun(
        image="cytopia/ansible:latest",
        command=prompt)


@up.hookimpl
def containers_for_prompt(prompt):
    return up.if_prompt_matches(run_container, prompt, "ansible")
