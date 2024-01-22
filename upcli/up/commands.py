import sys
import pkgutil
from pathlib import Path
from ruamel.yaml import YAML
from typing import TypeAlias
from collections.abc import Callable, Iterator
from importlib.util import find_spec

from uplib import Prompt
from up.help_texts import list_help_text, details_help_text, prompts_help_text

yaml=YAML()

Arguments: TypeAlias = list[str]
Commands: TypeAlias = dict[str, tuple[Callable[[Arguments], None], str]]

def _get_prompts(plugin_name: str) -> Iterator[dict]:
    plugin_path = Path(find_spec(f"up_{plugin_name}").origin).parent
    prompts_path = Path(plugin_path, 'up.yaml')
    try:
        with open(prompts_path, 'r') as file:
            prompts = (yaml.load(file))['prompts']
        for prompt in prompts:
            yield prompt
    except FileNotFoundError:
        raise FileNotFoundError("Plugin doens't have yaml file!")

def _list_plugins(args: Arguments):
    """
    Shows all installed plugins
    """
    plugins = []
    for pkg in pkgutil.iter_modules():
        if pkg.name.startswith("up_"):
            plugins.append(pkg.name)
    print("Installed plugins:")
    print("\n".join(plugins))

def _list_prompts(args: Arguments):
    """
    Shows the prompts from up.yaml of a plugin
    """
    for prompt in _get_prompts(args[0]):
        yaml.dump(prompt, sys.stdout)
    
def _prompt_details(args: Arguments):
    """
    Shows the prompt configuration from up.yaml of a plugin
    """
    for prompt in _get_prompts(args[0]):
        if prompt['prompt'] == ' '.join(args):
            yaml.dump(prompt, sys.stdout)
            break
        
_commands: Commands = {
    "list": (_list_plugins, list_help_text),
    "prompts": (_list_prompts, prompts_help_text),
    "details": (_prompt_details, details_help_text),
}

def _get_command_description(command:str) -> str:
    description = _commands[command][0].__doc__.replace('\n','')
    return description.lstrip()

def cmd_in_prompt(prompt: Prompt) -> bool:
    reserved_keyword = prompt[0]
    if reserved_keyword != 'plugin' or len(prompt) <= 1:
        return False
    command = prompt[1]
    match command:
        case cmd if cmd in _commands.keys():
            return True
        case _:
            raise Exception('Command not found!')

def run_cmd(command: str, arguments: Arguments):
    if len(arguments) == 1 and '--help' in arguments or '-h' in arguments:
        cmd_description = _get_command_description(command)
        print(_commands[command][1] % cmd_description)
        exit(0)
    _commands[command][0](arguments)
    exit(0)
