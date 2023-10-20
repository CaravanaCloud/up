import logging as log
import docker

from up_cli import RunConfig

class DockerContainers:
    def run(self, run: RunConfig):
        log.debug("Running container: %s", run)
        client = docker.from_env()
        #TODO: Catch errors, print properly, pass all params
        result = client.containers.run(
            image=run.image, 
            command=run.command,
            auto_remove=run.auto_remove)        
        log.info("container result")
        log.info("%s", result)
        log.debug("Container run done")
        
class Containers:
    delegate = DockerContainers()
    
    def run(self, run: RunConfig):
        self.delegate.run(run)
