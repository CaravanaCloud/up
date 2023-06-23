import os

_default_ssh_key = "~/.ssh/id_rsa.pub"

def lookup_ssh_key(var_name:str) -> str:
    if exists(_default_ssh_key):
        return read_file(_default_ssh_key)
    return None
    

def exists(path:str) -> bool:
    return os.path.exists(os.path.expanduser(path))


def read_file(path:str) -> str:
    with open(os.path.expanduser(path), "r") as f:
        return f.read()

