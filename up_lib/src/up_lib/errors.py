from enum import Enum

class Errors(Enum):
    NO_COMMAND = (1, "No command specified.")
    NO_DOCLET = (2, "No doclet specified.")

    def __call__(self):
        return UpException(self)

class UpException(Exception):
    def __init__(self, err):
        self.err = err

    def __repr__(self):
        return self.err
