from .log import *
import shlex


def parse_action(args):
    """Parse a line into an action, options, and prompt.
    This is the general expected format of an up expression:
    ACTION --OPT1=VAL1 --OPT2=VAL2: PROMPT
    for example:
    wait --timeout=5: aws sts get-caller-identity
    """
    debug(f"Parsing {type(args)} {args}")
    if type(args) == str:
        args = [args]
    if type(args) != list:
        args = list(args)
    if len(args) == 1:
        args = shlex.split(args[0])
    debug(f"Parsing input {type(args)} {args}")
    action = ""
    prompt = []
    options = {}
    lhs = True
    for arg in args:
        arg = arg.lstrip()
        if lhs:
            if arg.endswith(":"):
                lhs = False
                arg = arg[:-1]
            if str(arg).startswith("--"):
                option = arg[2:]
                keys = option.split("=")
                key = keys[0]
                value = keys[1] if len(keys) > 1 else True
                options[key] = value
            else:
                action += arg
        else:
            prompt.append(arg)
    action = action.lower()
    return action, options, prompt

def parse_command(prompt:list[str]) -> tuple:
    """Parse a command into a command and options.
    Used by internal commands (fibo --x=3)
    """
    debug(f"Parsing {type(prompt)} {prompt}")
    if type(prompt) == str:
        prompt = [prompt]
    if type(prompt) != list:
        prompt = list(prompt)
    if len(prompt) == 1:
        line = prompt[0]
        prompt = shlex.split(line)
    debug(f"Parsing input {type(prompt)} {prompt}")
    command = []
    options = {}
    for arg in prompt:
        arg = arg.strip()
        if str(arg).startswith("--"):
            option = arg[2:]
            keys = option.split("=")
            key = keys[0]
            value = keys[1] if len(keys) > 1 else True
            options[key] = value
        else:
            command.append(arg)
    return tuple(command), options
