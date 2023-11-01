import logging as log
import importlib
import pkgutil
import pluggy

from . import  hookspec
from .containers import Containers
from .hookspecs import run_for_prompt

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
    #    pm.load_setuptools_entrypoints("up")
    # pm.add_hookspecs(hookspec)
    log.debug("Plugins loaded.") 
    log.debug(str(pm.get_plugins()))