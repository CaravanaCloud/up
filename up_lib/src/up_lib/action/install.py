from ..log import *
from ..utils import get_sysinfo

from typing import Callable
from enum import Enum
from dataclasses import dataclass, astuple

InstallOptions = dict[str, int | str | bool]
InstallResult = dict
InstallKey = str
InstallHandler = Callable[[InstallKey, InstallOptions], InstallResult]

class InstallerType(Enum):
    WEB = "web",
    DNF = "dnf",
    YUM = "yum",
    APT = "apt",
    PIP = "pip",
    BREW = "brew"

@dataclass
class Installer:
    package_name: str
    installer_type: str
    package_version: str
    base_url: str
    package_urls: dict[str, str]
    verify_cmd: str

# TODO: Consolidate global state in a single class
_installers = {}

def install(opts: dict, prompt: list[str]) -> dict:
    trace("Invoking install action %s with %s options and %s installers", prompt, len(opts), len(_installers))
    result = [install_each(opts, package) for package in prompt]
    return {}

def install_each(opts: dict, package: str) -> dict:
    trace("Installing package %s with %s options", package, len(opts))
    if package not in _installers:
        warning(f"Package {package} not found")
        return {}
    installer = _installers.get(package)
    # TODO: Implement installers
    sysinfo = get_sysinfo()
    info("Installing %s for %s using %s", package, sysinfo, installer.installer_type)
    return {}

def register_install(package_name: str,
                     installer_type: str,
                     package_version: str,
                     base_url: str,
                     package_urls: dict[str, str],
                     verify_cmd: str) -> None:
    _installer_type = InstallerType[installer_type.upper()]
    installer = Installer(package_name, 
                          _installer_type, 
                          package_version, 
                          base_url, 
                          package_urls, 
                          verify_cmd)
    _installers[package_name] = installer
    trace("Added installer for %s, %s installers total", package_name, len(_installers))
    