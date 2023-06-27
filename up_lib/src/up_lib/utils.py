import os

def path_exists(path:str) -> bool:
    return os.path.exists(os.path.expanduser(path))


def read_file(path:str) -> str:
    with open(os.path.expanduser(path), "r") as f:
        return f.read()