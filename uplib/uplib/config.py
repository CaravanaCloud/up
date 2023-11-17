import pkgutil
import logging

from dynaconf import Dynaconf
from dynaconf.loaders import yaml_loader
from enum import Enum

class Settings:
    _settings = {}
    
    settings = None
    
    @classmethod
    def of_default_settings(cls):
        settings = Settings._settings.get("__DEFAULT__")
        if not settings:
            logging.info("Loading default settings")
            settings = Dynaconf(
                    environments=False,
                    envvar_prefix="UP")
            up_yaml = pkgutil.get_data(__name__, "up.yaml")
            if up_yaml:
                up_yaml = up_yaml.decode("utf-8")
                yaml_loader.load(settings, filename=up_yaml)
            Settings._settings["__DEFAULT__"] = settings
        return settings

    @classmethod
    def prefix_for(cls, plugin_mod):
        plugin_name = plugin_mod.__name__
        plugin_name = plugin_name.replace("-", "_")
        plugin_name = plugin_name.upper()
        return plugin_name

    @classmethod
    def of_plugin_settings(cls, plugin_name, settings_path):
        settings = Settings._settings.get(plugin_name)
        if not settings:
            env_prefix = Settings.prefix_for(plugin_name)
            settings = Dynaconf(
                load_dotenv=True,
                envvar_prefix=env_prefix,
                settings_file=settings_path,)
            Settings._settings[plugin_name] = settings
        return settings
    
    def __init__(self, plugin_name = None, settings_path = None):
        if plugin_name:
            self.settings = Settings.of_plugin_settings(plugin_name, settings_path)
        else:
            self.settings = Settings.of_default_settings()
    
    def settings(self) -> Dynaconf:
        return self.settings
    
    def get(self, config_enum):
        config = config_enum.value
        default_val = config[1] if len(config) > 1 else None
        config_key = config[0]
        result = self._settings.get(config_key, default_val)
        if result:  
            converter = config[2] if len(config) > 2 else None
            if converter:
                result = converter(result)
        return result

class Config(Enum):
    # (key, default_value)
    default_image = ("default_image", "fedora")
    welcome_message = ("welcome_message", "Thank your for running UP!")
    log_level = ("log_level", "INFO")
    volumes = ("volumes", {})
    ports = ("ports", {})
    prompts = ("prompts", [])
    
    # Gets a configuration value from default settings
    def get(self):
        result = Settings().get(self)
        return result


def get_log_level():
    return Config.log_level.get()


