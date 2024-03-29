import importlib
from logging import debug
import pkgutil
import os
import pluggy
import json

from . import settings_maps
from .containers import Containers
from .hookspecs import containers_for_prompt
from .logging import log
from .config import Settings, Config


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
        raise e
        plugin_name = None
    return (plugin_name, settings_file)


def load_settings(plugin_name, settings_path):
    settings = Settings(plugin_name, settings_path)
    prompts = settings.settings.get("prompts")
    #prompts = settings.get(Config.prompts)
    # Load Environment Variables
    log.debug("Loading %s prompts: %s", len(prompts), prompts)
    load_prompts(prompts, settings)
    log.info("Loaded settings for plugin %s@%s\n%s", plugin_name, settings_path, str(settings))
    return settings

def load_prompts(prompts, settings):
    for prompt_cfg in prompts:
        load_prompt(prompt_cfg)
        load_volumes(prompt_cfg)
        load_ports(prompt_cfg)
        plugin_name = prompt_cfg.get('prompt').split()[0]
        log.debug("use default volumes? %s", prompt_cfg.get("default_volumes"))
        if prompt_cfg.get("default_volumes"):
            settings_maps[plugin_name].update({"volumes": settings.settings.get("volumes", {})})
        log.debug("use default ports? %s", prompt_cfg.get("default_ports"))
        if prompt_cfg.get("default_ports"):
            settings_maps[plugin_name].update({"ports": settings.settings.get("ports", {})})

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
        log.debug(settings_map)

def load_volumes(prompt):
    log.debug("Loading volumes")
    settings_map = settings(prompt.get('prompt'))
    volumes = settings_map.get("volumes")
    if not volumes:
        settings_map["volumes"] = Config.volumes.get() | prompt.get('volumes', {})

def load_ports(prompt):
    log.debug("Loading ports")
    settings_map = settings(prompt.get('prompt'))
    ports = settings_map.get("ports")
    if not ports:
        settings_map["ports"] = Config.ports.get() | prompt.get('ports', {})
    log.debug(settings_map)

def settings(prompt):
    #TODO: Delegate to Settings.of_prompt(prompt)
    #TODO: Create type-safe PromptConfig enum?
    plugin_name = prompt.split()[0]
    plugin_map = settings_maps.get(plugin_name, {})
    if not plugin_map:
        settings_maps[plugin_name] = plugin_map
    settings_map = plugin_map.get(prompt, {})
    if not settings_map:
        plugin_map[prompt] = settings_map
    return settings_map
