import sys
import logging as log
import up_lib


def print_help():
    log.debug("Please please help me")


def exit_cli(param):
    code = 0
    if param:
        log.error(param)
        code = 1
    sys.exit(code)


def main():
    log.basicConfig(level=log.DEBUG)
    args = sys.argv
    len_args = len(args)
    if len_args < 1:
        print_help()
        exit_cli("NO_COMMAND_SPECIFIED")
    executable = args[0]
    line = args[1:]
    log.debug(f"executable: {executable}")
    log.debug(f"line: {line}")
    context = {
        "executable": executable
    }
    up_lib.up(line= line,
              context= context)


if __name__ == '__main__':
    main()

