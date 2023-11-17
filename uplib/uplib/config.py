import pkgutil
import logging

from dynaconf import Dynaconf
from dynaconf.loaders import yaml_loader
from enum import Enum

class Config(Enum):
    # (key, default_value)
    default_image = ("default_image", "fedora")
    welcome_message = ("welcome_message", "Thank your for running UP!")
    log_level = ("log_level", "INFO", logging.getLevelName)
    volumes = ("volumes", {})
    ports = ("ports", {})

    __settings = None

    #TODO: Add optional prompt
    @classmethod
    def settings(cls):
        _settings = Config.__settings
        if not _settings:
            _settings = Dynaconf(
                    environments=False,
                    envvar_prefix="UP")
            up_yaml = pkgutil.get_data(__name__, "up.yaml")
            if up_yaml:
                up_yaml = up_yaml.decode("utf-8")
                yaml_loader.load(_settings, filename=up_yaml)
        return _settings

    def get(self):
        value = self.value
        key = value[0]
        result = Config.settings().get(key)
        if not result:
            result = value[1] if len(value) > 1 else None
        converter = value[2] if len(value) > 2 else None
        if converter and result:
            result = converter(result)
        return result

def get_log_level():
    return Config.log_level.get()


