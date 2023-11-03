import docker
import subprocess
from dataclasses import dataclass, field
from typing import TypeAlias
from .logging import log

# https://docker-py.readthedocs.io/en/stable/containers.html
@dataclass
class ContainerRun:
    name: str = field(kw_only=True, default="")
    image: str = field(kw_only=True, default="")
    command: list[str]  = field(kw_only=True, default_factory=list)
    environment: dict[str, str]  = field(kw_only=True, default_factory=dict)
    ports: dict[str, str]  = field(kw_only=True, default_factory=dict)
    volumes: dict[str, str]  = field(kw_only=True, default_factory=dict)
    auto_remove: bool  = field(kw_only=True, default=True)
    network_mode: str  = field(kw_only=True, default="host")

ContainerRuns:TypeAlias = list[ContainerRun]


class DockerContainers:
    def run(self, run: ContainerRun):
        log.info("Running container: %s", run)
        client = docker.from_env()
        #TODO: Catch errors, print properly, pass all params
        #TODO: Locate bash properly
        #TODO: Consider if every command should be auto-wrapped in bash (perhaops detect if contains pipes or redirects)
        command = ["sh", "-c", subprocess.list2cmdline(run.command)]
        log.debug("$: %s", run)
        
        try:
            result = client.containers.run(
                image=run.image, 
                command= command,
                auto_remove=run.auto_remove)
            log.info("container result: \n %s", result)
            
        except Exception as e:
            log.error("Failed to run container")
            log.debug("%s", run)
            log.error("%s", e)
        
class Containers:
    delegate = DockerContainers()
    
    def run(self, run: ContainerRun):
        self.delegate.run(run)
