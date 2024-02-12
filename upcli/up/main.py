import sys
from datetime import datetime

import uplib
from up.__version__ import version
from up.options import setup_options
from up.help_texts import up_help_text
from up.utils import get_commands_information
from up.commands import cmd_in_prompt, run_cmd

log = uplib.log

def _print_up_help(args) -> bool:
    if len(args) == 2:
        if args[1] == "--help" or args[1] == "-h":
            return True
    return False

def exit_cli(code=-1):
    if code:
        log.error("Exiting up cli with code %s", code)
    sys.exit(code)

def cli_main():
    now = datetime.now()
    log.info(f"Starting UP cli at {now.isoformat()}")
    args = sys.argv
    if len(args) <= 1 or _print_up_help(args):
        print(up_help_text % (version, get_commands_information()))
        exit(0)
    executable = args[0]
    prompt = args[1:]
    if cmd_in_prompt(prompt):
        run_cmd(prompt[1], prompt[2:])
    context = {"executable": executable}
    try:
        prompt_without_options = setup_options(prompt)
        print(prompt_without_options)
        uplib.up_main(context, prompt_without_options)
    except Exception as e:
        log.error(e)
        # print stack trace
        raise e
        exit_cli("UP_ERROR")
        
