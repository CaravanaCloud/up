from .log import *
import shlex


def parse(args):
    debug(f"Parsing {type(args)} {args}")
    if type(args) == str:
        args = [args]
    if type(args) != list:
        args = list(args)
    if len(args) == 1:
        args = shlex.split(args[0])
    command = ""
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
                command += arg
        else:
            prompt.append(arg)
    command = command.lower()
    return command, options, prompt

