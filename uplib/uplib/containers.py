import re
import docker
import subprocess

from dataclasses import dataclass, field
from typing import TypeAlias
from .logging import log
from datetime import datetime

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
    # Feature Flags
    bash_wrap: bool = field(kw_only=True, default=False)

ContainerRuns:TypeAlias = list[ContainerRun]


class DockerContainers:
    def run(self, run: ContainerRun):
        log.info("Running container: %s", run)
        client = docker.from_env()
        #TODO: Catch errors, print properly, pass all params
        #TODO: Locate bash properly
        #TODO: Consider if every command should be auto-wrapped in bash (perhaops detect if contains pipes or redirects)
        command = run.command
        if (run.bash_wrap):
            command = ["sh", "-c", subprocess.list2cmdline(command)]
        log.debug("$: %s", run)
        name = run.name if run.name else generate_container_name(run)
        try:
            container = client.containers.run(
                name=name,
                image=run.image, 
                command= command,
                auto_remove=run.auto_remove,
                detach=True)
            for line in container.logs(stream=True):
                line = line.decode("utf-8").strip()
                log.info("%s", line)
            container.wait()
            log.debug("container ended.")
            
        except Exception as e:
            log.error("Failed to run container")
            log.debug("%s", run)
            log.error("%s", e)

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
