import os

def path_exists(path:str) -> bool:
    return os.path.exists(os.path.expanduser(path))


def read_file(path:str) -> str:
    with open(os.path.expanduser(path), "r") as f:
        return f.read()

def get_sysinfo():
    uname = os.uname()
    std_sysname = uname.sysname.lower()
    std_arch = uname.machine.lower()
    return std_sysname + "-" + std_arch


# print(get_sysinfo())
