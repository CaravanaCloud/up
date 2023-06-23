from .log import *
from .actions import *
import shlex

def parse_action(line = None, actions = []):
    """Parse a line into an action, options, and prompt.
    This is the general expected format of an up expression:
    ACTION --OPT1=VAL1 --OPT2=VAL2: PROMPT
    for example:
    wait --timeout=5: aws sts get-caller-identity
    """
    tokens:list = []
    if type(line) == str:
        tokens = shlex.split(line)
    if type(line) == list:
        if len(line) == 1:
            tokens = shlex.split(line[0])
        else:
            tokens = line
    debug(f"Parsing {type(line)} {tokens} with {len(tokens)} tokens and {len(actions)} actions")
    action = ""
    prompt = []
    options = {}
    lhs = True

    for (index, token) in enumerate(tokens):
        parse_action = "?"
        if token.endswith(":"):
            token = token[:-1]
        if index:
            if lhs:
                if str(token).startswith("--"):
                    option = token[2:]
                    keys = option.split("=")
                    key = keys[0]
                    value = keys[1] if len(keys) > 1 else True
                    options[key] = value
                    parse_action = "set_option"
                else:
                    lhs = False
                    prompt.append(token)
                    parse_action = "terminate_lhs"
            else:
                prompt.append(token)
                parse_action = "append_prompt"
        else:
            action = token.strip().lower()
            if token in actions:
                debug(f"Parsed action {token}")
            else:
                warning(f"Parsed unknown action {token}")
            parse_action = "set_action"
        debug(f"Parsing lhs={lhs} [{index} {token}] => {parse_action}")

    result = Action(action, options, prompt)
    debug(f"Parser result: {result}")
    return result


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
