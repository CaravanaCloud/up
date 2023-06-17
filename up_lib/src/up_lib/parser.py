from .log import *
import shlex

# TODO: improve parser to take "wait --atMost=5 cowsay hello" as "wait --atMost=5: cowsay hello"
def parse_action(line = None, actions = []):
    """Parse a line into an action, options, and prompt.
    This is the general expected format of an up expression:
    ACTION --OPT1=VAL1 --OPT2=VAL2: PROMPT
    for example:
    wait --timeout=5: aws sts get-caller-identity
    """
    if type(line) == str:
        line = [line]
    if type(line) != list:
        line = list(line)
    if len(line) == 1:
        line = shlex.split(line[0])
    debug(f"Parsing {type(line)} {line} with {len(actions)} actions")

    action = ""
    prompt = []
    options = {}
    lhs = True
    token = line[0].strip()

    for (index, token) in enumerate(line):
        debug(f"Parsing {index} {token} | lhs {lhs}")
        if not lhs:
            prompt.append(token)
        else:
            if token.endswith(":"):
                lhs = False
                token = token[:-1]
            if index == 0:
                token = token.lower()
                if token in actions:
                    debug(f"Parsed action {token}")
                    action = token
                else:
                    debug(f"Unknown action {token}")
                    
            if str(token).startswith("--"):
                option = token[2:]
                keys = option.split("=")
                key = keys[0]
                value = keys[1] if len(keys) > 1 else True
                options[key] = value
    action = action.lower()
    result = (action, options, prompt,)
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
