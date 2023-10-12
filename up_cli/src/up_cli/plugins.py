import logging as log
import importlib
import pkgutil

from up_cli import pm, hookspec
from .defaults import image_for_prompt

def load_plugins(context):
    log.info("Loading plugins")
    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('up_')
    }
    log.info("Discovered %s plugins: %s", len(discovered_plugins), discovered_plugins)
    # create a manager and add the spec
    pm.add_hookspecs(hookspec)
    pm.load_setuptools_entrypoints("up")
    pm.register(image_for_prompt)
    log.debug("Plugins loaded.") 
    log.debug(str(pm.get_plugins()))