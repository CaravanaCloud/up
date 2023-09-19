import pytest
from up_lib.lookups import *

def read_file(filename:str) -> str:
    with open(filename, "r") as f:
        return f.read()

def load_readme(var_name:str) -> str:
    return read_file("../README.md")

def test_lookup_registered():
    # given
    register_lookup("README", load_readme)
    # when
    value = lookup("README")
    # then
    assert len(value) > 42
