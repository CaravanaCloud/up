import sys
import logging as log
from up_lib import up


def print_help():
    log.debug("Please please help me")


def exit_cli(param):
    code = 0
    if param:
        log.error(param)
        code = 1
    sys.exit(code)


def main():
    args = sys.argv
    len_args = len(args)
    if len_args < 1:
        print_help()
        exit_cli("NO_COMMAND_SPECIFIED")
    log.basicConfig(level=log.DEBUG)
    executable = args[0]
    prompt = args[1:]
    log.debug(f"executable: {executable}")
    log.debug(f"prompt: {prompt}")
    up(prompt)


if __name__ == '__main__':
    main()

