from dynaconf import Dynaconf
import logging
from . import settings_files

_settings = None
def settings():
    global _settings
    if not _settings:
        _settings = Dynaconf(
                environments=True,
                envvar_prefix="UP",
                settings_files=settings_files
            ) 
    return _settings

def get_log_level():
    level_name = settings().get("log_level", "INFO")
    level = logging.getLevelName(level_name)
    return level


