import logging as log
from dataclasses import dataclass
import docker

@dataclass
class ContainerRun:
    """Specify the parameters for a container run"""
    image: str
    prompt: list[str]


class DockerContainers:
    def run(self, run: ContainerRun):
        log.debug("Running container: %s", run)
        client = docker.from_env()
        image = run.image
        prompt = run.prompt
        #TODO: Catch errors, print properly
        result = client.containers.run(
            image=image, 
            command=prompt,
            auto_remove=True)        
        log.info("container result")
        log.info("%s", result)
        log.debug("Container run done")
        
class Containers:
    delegate = DockerContainers()
    
    def run(self, run: ContainerRun):
        self.delegate.run(run)