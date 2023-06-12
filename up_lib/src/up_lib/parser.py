from .log import *
from .command import *


def parse(args):
    debug(f"Parsing {type(args)} {args}")
    if type(args) == str:
        args = args.split(" ")
    if type(args) != list:
        args = list(args)
    command = []
    prompt = []
    options = {}
    lhs = True
    for arg in args:
        arg = arg.lstrip()
        if lhs:
            if str(arg).startswith("--"):
                option = arg[2:]
                keys = option.split("=")
                key = keys[0]
                value = keys[1] if len(keys) > 1 else True
                if value.endswith(":"):
                    value = value[:-1]
                options[key] = value
            else:
                command.append(arg)
        else:
            prompt.append(arg)
        if lhs and arg.endswith(":"):
            lhs = False
    cmd = Command(tuple(command), options, prompt)
    return cmd
