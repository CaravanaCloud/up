import pluggy
from .containers import Containers

hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")
containers = Containers()

def match_prompt(prompt, head, image):
    if not prompt:
        return None
    if prompt[0] == head:
        return image
    return None
