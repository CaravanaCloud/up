import importlib
import pkgutil
import pluggy

from . import hookspec
from .containers import Containers
from .hookspecs import containers_for_prompt
from .logging import log


def load_plugins(context):
    log.info("Loading plugins")
    discovered_plugins = {
        name: importlib.import_module(name)
            for finder, name, ispkg
            in pkgutil.iter_modules()
            if name.startswith('up_')
    }
    # for each plugin, seach its contents for all configuration files named up.yaml
    plugin_names = discovered_plugins.keys()
    for plugin_name in plugin_names:
        load_plugin(plugin_name)    
    log.info("Discovered %s plugins: %s", len(plugin_names), str(plugin_names))
    # create a manager and add the spec
    #    pm.load_setuptools_entrypoints("up")
    # pm.add_hookspecs(hookspec)
    # log.debug("Plugins loaded.")
    # log.debug(str(pm.get_plugins()))

def load_plugin(plugin_name):
    log.info("Loading plugin %s", plugin_name)
    try:
        cfg = pkgutil.get_data(plugin_name, "up.yaml")
    except FileNotFoundError:
        log.info("No up.yaml found in plugin %s", plugin_name)
        cfg = None
    if cfg:
        print(str(cfg))    
