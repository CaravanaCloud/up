import os
from ..utils import *

_default_ssh_key = "~/.ssh/id_rsa.pub"

def lookup_ssh_key(var_name:str) -> str:
    if path_exists(_default_ssh_key):
        return read_file(_default_ssh_key)
    return None
    


