import importlib
import pkgutil
import os
import pluggy
import json
from dynaconf import Dynaconf

from . import settings_maps
from .containers import Containers
from .hookspecs import containers_for_prompt
from .logging import log


def load_plugins(context):
    log.debug("Loading plugins")
    plugin_names = []
    settings_files = []
    for finder, name, ispkg in pkgutil.iter_modules():
        if name.startswith('up_'):
            plugin_mod = importlib.import_module(name)
            plugin_names.append(name)
            plugin_path = os.path.dirname(plugin_mod.__file__)
            plugin_ok, settings_ok = load_plugin(plugin_mod, plugin_path)
            if plugin_ok:
                plugin_names.append(plugin_ok)
            if settings_ok:
                settings_files.append(settings_ok)
    log.debug("Discovered %s plugins: %s", len(
        plugin_names), str(plugin_names))
    log.debug("Discovered %s config files: %s", len(
        settings_files), str(settings_files))
    # create a manager and add the spec
    # TODO: Check if this is needed pm.load_setuptools_entrypoints("up")
    # TODO: Check if this is needed pm.add_hookspecs(hookspec)


def load_plugin(plugin_name, plugin_dir):
    log.debug("Loading plugin %s:%s", plugin_name, plugin_dir)
    settings_file = None
    try:
        plugin_file = "up.yaml"
        settings_path = plugin_dir + "/" + plugin_file
        file_exists = os.path.isfile(settings_path)
        if file_exists:
            log.debug("Loading settings from %s:%s",
                      plugin_name, settings_path)
            load_settings(plugin_name, settings_path)
        else:
            log.debug("No settings file found on %s:%s",
                      plugin_name, plugin_dir)
    except Exception as e:
        log.error("Error loading plugin %s: %s", plugin_name, str(e))
        plugin_name = None
    return (plugin_name, settings_file)


def load_settings(plugin_name, settings_path):
    env_prefix = prefix_for(plugin_name)
    settings = Dynaconf(
        load_dotenv=True,
        envvar_prefix=env_prefix,
        settings_file=settings_path,)
    # Load Environment Variables
    prompts = settings.get("prompts", [])
    log.debug("Loading %s prompts: %s", len(prompts), prompts)
    load_prompts(prompts)
    # Load Volumes
    # Load Ports
    # ...
    log.debug("Settings loaded")
    settings_json = json.dumps(settings_maps, indent=2)
    log.info("Loaded settings\n%s", settings_json)
    return settings


def prefix_for(plugin_mod):
    plugin_name = plugin_mod.__name__
    plugin_name = plugin_name.replace("-", "_")
    plugin_name = plugin_name.upper()
    return plugin_name

def load_prompts(prompts):
    for prompt_cfg in prompts:
        load_prompt(prompt_cfg)

def load_prompt(prompt_cfg):
    log.debug("Loading prompt %s", prompt_cfg)  
    prompt = prompt_cfg.get("prompt")
    if not prompt:
        log.error("Prompt not defined in %s", prompt_cfg)
        return
    env = prompt_cfg.get("env", [])
    match env:
        case list():
            load_env_list(prompt, env)

def load_env_list(prompt, env):
    log.debug("Loading environment list for prompt [%s]", prompt)
    settings_map = settings(prompt)
    env_map = settings_map.get("env")
    if not env_map:
        env_map = {}
        settings_map["env"] = env_map
    for var in env:
        log.debug("Loading environment variable [%s]", var)
        env_map[var] = {}
        
def settings(prompt):
    settings_map = settings_maps.get(prompt)
    if not settings_map:
        settings_map = {}
        settings_maps[prompt] = settings_map
    return settings_map