import pkgutil
import logging

from dynaconf import Dynaconf
from dynaconf.loaders import yaml_loader
from enum import Enum

class Config(Enum):
    default_image = "default_image"
    welcome_message = "welcome_message"
    log_level = "log_level"
    
    def get(self):
        key = self.value
        return settings().get(key)

_settings = None
def settings():
    global _settings
    if not _settings:
        _settings = Dynaconf(
                environments=False,
                envvar_prefix="UP")
        up_yaml = pkgutil.get_data(__name__, "up.yaml")
        if up_yaml:
            up_yaml = up_yaml.decode("utf-8")
            yaml_loader.load(_settings, filename=up_yaml)
    return _settings

def get_log_level():
    level_name = settings().get("log_level", "INFO")
    level = logging.getLevelName(level_name)
    return level

