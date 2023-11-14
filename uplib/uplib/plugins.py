import importlib
import pkgutil
import os
import pluggy
import json
from dynaconf import Dynaconf

from .containers import Containers
from .hookspecs import containers_for_prompt
from .logging import log


def load_plugins(context):
    log.info("Loading plugins")
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
    log.debug("Discovered %s plugins: %s", len(plugin_names), str(plugin_names))
    log.debug("Discovered %s config files: %s", len(settings_files), str(settings_files))
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
            log.debug("Loading settings from %s:%s", plugin_name, settings_path)
            settings = load_settings(plugin_name, settings_path)
            settings_file = settings_path
        else:
            log.debug("No settings file found on %s:%s", plugin_name, plugin_dir)
    except Exception as e:
        log.error("Error loading plugin %s: %s", plugin_name, str(e))
        plugin_name = None
    return (plugin_name, settings_file)

def load_settings(plugin_name, settings_path):
    env_prefix = prefix_for(plugin_name)
    settings = Dynaconf(
        load_dotenv=True,
        envvar_prefix = env_prefix, 
        settings_file=settings_path,
    )
    # Load Environment Variables
    prompts = settings.get("prompts", [])
    log.info("Loading %s prompts: %s", len(prompts), prompts)
        
    # Load Volumes
    # Load Ports
    # ...
    log.info("Settings loaded "+str(type(settings)))
    return settings



def prefix_for(plugin_mod):
    plugin_name = plugin_mod.__name__
    plugin_name = plugin_name.replace("-", "_")
    plugin_name = plugin_name.upper()
    return plugin_name