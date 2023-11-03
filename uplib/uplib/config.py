from dynaconf import Dynaconf
import logging

settings = Dynaconf(
    envvar_prefix="UP",
    settings_files=['settings.toml', '.secrets.toml']
)

def get_log_level():
    level_name = settings.get("log_level", "INFO")
    level = logging.getLevelName(level_name)
    return level


