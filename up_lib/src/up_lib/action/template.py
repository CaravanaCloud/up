from ..log import *
from ..utils import *

def template(opts: dict, prompt: list[str]) -> dict:
    trace("Template action %s with %s options", prompt, len(opts))
    for template_name in prompt:
        process_template(template_name)
    return {}


def process_template(template_name:str):
    trace("Processing template: %s", template_name)
    if not path_exists(template_name):
        error("template not found %s", template_name)
        raise FileNotFoundError(f"template not found {template_name}")
    return process_file(template_name)


def process_file(template_name:str):
    if (".env." in template_name) or (".envsubst." in template_name):
        return process_envsubst(template_name)
    raise ValueError(f"Unknown template type for file. {template_name}")


def process_envsubst(template_name:str):
    debug(f"Processing envsubst. {template_name}")
    lookup_variables(template_name)
    # invoke_envsubst()
    # validate_result()
    return {}

def lookup_variables(template_name:str):
    debug(f"Looking up variables in template. {template_name}")
    variables = []
    with open(template_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.startswith('$'):
                    variables.append(word[1:])
    debug(f"Looking up variables: {variables}")
    # LOOKUP VARS
    return {}
