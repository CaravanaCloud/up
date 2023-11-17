import uplib as up
import os

def get_homedir():
    return os.environ['HOME']

def run_container(prompt, command=None, working_dir=None):
    _command = command if command else prompt
    _working_dir = working_dir if working_dir else "/"
    return up.ContainerRun(
        image="caravanacloud/up_aws",
        bash_wrap=False,
        volumes = {
            get_homedir()+"/.aws":{
                "bind":"/root/.aws",
                "mode":"ro"
            }
        },
        working_dir = _working_dir,
        command=_command
    )

def lookup_container(prompt):
    match prompt:
        case ["subs", *rest]:
            return run_container(rest, 
                                 working_dir="/opt/aws_utils/",
                                 command=["/home/up_user/.local/bin/poetry", "run", "subs"])
    return run_container(prompt)


@up.hookimpl
def containers_for_prompt(prompt):
    match prompt:
        case ["aws", *rest]:
            return lookup_container(rest)
    return None
