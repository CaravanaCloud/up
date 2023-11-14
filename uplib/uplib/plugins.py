import importlib
import pkgutil
import os
import pluggy

from . import settings_files
from .containers import Containers
from .hookspecs import containers_for_prompt
from .logging import log


def load_plugins(context):
    log.info("Loading plugins")
    plugin_names = []
    for finder, name, ispkg in pkgutil.iter_modules():
        if name.startswith('up_'):
            plugin_name = importlib.import_module(name)
            plugin_names.append(name)
            plugin_path = os.path.dirname(plugin_name.__file__)
            load_plugin(plugin_name, plugin_path)    
    log.info("Discovered %s plugins: %s", len(plugin_names), str(plugin_names))
    log.info("Discovered %s config files: %s", len(settings_files), str(settings_files))
    # create a manager and add the spec
    # TODO: Check if this is needed pm.load_setuptools_entrypoints("up")
    # TODO: Check if this is needed pm.add_hookspecs(hookspec)
    

def load_plugin(plugin_name, plugin_path):
    log.info("Loading plugin %s from %s", plugin_name, plugin_path)
    try:
        plugin_file = plugin_path + "/up.yaml"
        file_exists = os.path.isfile(plugin_file)
        if file_exists:
            settings_files.append(plugin_file)
            log.info("Found up.yaml in plugin %s: %s", plugin_name, plugin_file)
        else:
            log.info("No up.yaml found in plugin %s: %s", plugin_name, plugin_file)
    except Exception as e:
        log.error("Error loading plugin %s: %s", plugin_name, str(e))
