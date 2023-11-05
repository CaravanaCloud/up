import uplib as up
import os

def get_homedir():
    return os.environ['HOME']

def run_container(prompt):
    return up.ContainerRun(
        image="amazon/aws-cli",
        bash_wrap=False,
        volumes = {
            get_homedir()+"/.aws":"/root/.aws"
        },
        command=prompt[1:])


@up.hookimpl
def containers_for_prompt(prompt):
    return up.if_prompt_matches(run_container, prompt, "aws")
