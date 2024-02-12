import re
from shlex import join

from uplib import options_map, Prompt

_options_pattern = re.compile(r'\-X\w+\=\S+')

def _have_options(prompt: Prompt) -> bool:
    if _options_pattern.match(join(prompt)):
        return True
    return False

def _match_value(pattern: str, string: str) -> str:
    value = re.match(pattern, string)
    return value.groups()[0]

def _set_ports(value: str):
    formated_value = value.split(':')
    options_map['ports'] = {formated_value[0]: formated_value[1]}

def _set_volumes(value: str):
    formated_value = value.split(':')
    volume_key = formated_value[0]
    volume_bind = formated_value[1].split(',')[0]
    volume_mode = formated_value[1].split(',')[1]
    options_map['volumes'] = {
        volume_key: {
            'bind': volume_bind,
            'mode': volume_mode,
        },
    }

_options = {
    'p': _set_ports,
    'v': _set_volumes,
}

def _set_option(option: str):
    key = _match_value(r'\-X(\w)', option)
    value = _match_value(r'\-X\w.(.+)', option)
    _options[key](value)

def setup_options(prompt: Prompt) -> Prompt:
    prompt_without_options = join(prompt)
    if _have_options(prompt):
        for option in _options_pattern.findall(join(prompt)):
            _set_option(option)
            prompt_without_options = _options_pattern.sub(
                '', prompt_without_options)
        return prompt_without_options.lstrip().split()
    return prompt
