import sys
import logging as log
from up_lib import up, Errors


def print_help():
    log.debug("Please please help me")


def exit_cli(error):
    code = 0
    if error:
        (code, msg) = error.value
        log.error(msg)
    sys.exit(code)


def main():
    log.basicConfig(level=log.DEBUG)
    args = sys.argv
    len_args = len(args)
    if len_args <= 1:
        print_help()
        exit_cli(Errors.NO_COMMAND)
    executable = args[0]
    prompt = args[1:]
    log.debug(f"executable: {executable}")
    log.debug(f"prompt: {prompt}")
    up(prompt)


if __name__ == '__main__':
    main()

