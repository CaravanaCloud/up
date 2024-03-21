import re
import os
import docker
import subprocess
from rich.console import Console
from rich.markup import escape

from dataclasses import dataclass, field
from typing import TypeAlias
from .logging import log
from datetime import datetime
from . import settings_maps, options_map

import sys

# https://docker-py.readthedocs.io/en/stable/containers.html
@dataclass
class ContainerRun:
    # Container Configuration
    name: str = field(kw_only=True, default="")
    image: str = field(kw_only=True, default="")
    command: list[str]  = field(kw_only=True, default_factory=list)
    environment: dict[str, str]  = field(kw_only=True, default_factory=dict)
    ports: dict[str, str]  = field(kw_only=True, default_factory=dict)
    volumes: dict[str, str]  = field(kw_only=True, default_factory=dict)
    auto_remove: bool  = field(kw_only=True, default=True)
    network_mode: str  = field(kw_only=True, default="host")
    user: str = field(kw_only=True, default="")
    # TODO: user
    working_dir: str  = field(kw_only=True, default="/")
    # Feature Flags
    bash_wrap: bool = field(kw_only=True, default=False)

ContainerRuns:TypeAlias = list[ContainerRun]


class DockerContainers:
    @classmethod
    def volumes_of(cls, run: ContainerRun, prompt: str):
        plugin_name = "__NOT_FOUND__"
        tokens = prompt.split()
        if len(tokens):
            plugin_name = tokens[0]
        log.debug("loading volumes for prompt: %s", prompt)

        plugin_settings = settings_maps.get(plugin_name, {})
        default_volumes = plugin_settings.get("volumes", {})
        settings_vols = default_volumes.to_dict() if default_volumes else {}
        if settings_maps.get(plugin_name, {}).get(prompt):
            settings_vols = settings_vols | settings_maps[plugin_name][prompt].get("volumes", {})
        cwd = os.getcwd()
        home = os.path.expanduser("~")
        default_vols = {
            home : {
                "bind": "/tmp/up_home",
                "mode": "rw"
            },
            cwd : {
                "bind": "/tmp/up_cwd",
                "mode": "rw"
            }
        }
        options_volumes = options_map.get('volumes', {})
        result = run.volumes | settings_vols | default_vols | options_volumes
        return result

    @classmethod
    def ports_of(cls, prompt: str):
        plugin_name = "__UNDEFINED__"
        tokens = prompt.split()
        if len(tokens):
            plugin_name = tokens[0]
        options_ports = options_map.get('ports', {})
        default_ports = settings_maps.get(plugin_name, {}).get("ports", {})
        ports = default_ports.to_dict() if default_ports else {}
        if settings_maps.get(plugin_name, {} ).get(prompt):
            ports = ports | settings_maps[plugin_name][prompt].get("ports", {})
        return ports | options_ports
    
    def run(self, run: ContainerRun):
        client = docker.from_env()
        #TODO: Catch errors, print properly, pass all params
        #TODO: Locate bash properly
        #TODO: Consider if every command should be auto-wrapped in bash (perhaops detect if contains pipes or redirects)
       
        command = run.command
        prompt = ' '.join(run.command)
        if (run.bash_wrap):
            command = ["sh", "-c", subprocess.list2cmdline(command)]
        log.debug("$: %s", run)
        name = run.name if run.name else generate_container_name(run)
        volumes = DockerContainers.volumes_of(run, prompt)
        ports = DockerContainers.ports_of(prompt)
        # TODO only pass user when sure (or defined by plugin)
        # user = "up_user"
        user = run.user
        working_dir = run.working_dir
        up_console = Console(file=sys.stderr)
        app_console = Console(file=sys.stdout)
        up_console.log(f"Running container: {name}")
        up_console.log({
            "name": name,
            "image": run.image, 
            "command":  command,
            "auto_remove": run.auto_remove,
            "volumes": volumes,
            "ports": ports,
            "user": user,
            "working_dir": working_dir,
            "detach": True
        })
        try:
            container = client.containers.run(
                name=name,
                image=run.image, 
                command= command,
                auto_remove=run.auto_remove,
                volumes=volumes,
                ports=ports,
                user=user,
                working_dir=working_dir,
                detach=True
            )
            for line in container.logs(stream=True):
                line = line.decode("utf-8").strip()
                app_console.print(escape(line))
            container.wait()
            log.debug("container ended.")
            
        except Exception as e:
            log.error("Failed to run container")
            log.debug("%s", run)
            log.error("%s", e)
            # raise e

_container_name_pattern = '[^a-zA-Z0-9_.-]'
def generate_container_name(run):
    timestamp = datetime.now().strftime("%H%M%S")
    image_name = run.image
    # replace all chars not valid ([a-zA-Z0-9][a-zA-Z0-9_.-]) with _
    image_name = re.sub(_container_name_pattern, '_', image_name)
    return f"up-{image_name}-{timestamp}"
        
class Containers:
    delegate = DockerContainers()
    
    def run(self, run: ContainerRun):
        self.delegate.run(run)
