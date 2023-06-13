from .log import *
import importlib
import pkgutil


def load_plugins():
    plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('up_')
    }
    for name, module in plugins.items():
        if hasattr(module, "up_init"):
            debug("Initializing module %s", name)
            module.up_init()
        else:
            debug("Module %s has no up_init, skipping", name)
    debug(f"Discovered {len(plugins)} plugins")
    debug(plugins)