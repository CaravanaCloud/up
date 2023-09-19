from .log import *
import importlib
import pkgutil


def load_plugins():
    module_prefix="up"
    plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith(module_prefix)
    }
    for name, module in plugins.items():
        if hasattr(module, "up_init"):
            trace("Initializing module %s", name)
            module.up_init()
        else:
            trace("Module %s has no up_init, skipping", name)
    debug(f"Discovered {len(plugins)} plugins")
