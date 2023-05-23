import logging as log
from .wait import wait
from .errors import Errors


def up(prompt):
    if len(prompt) == 0:
        print("ERROR")
        return
    doclet = prompt[0]
    log.debug(f"{doclet}: {prompt}")
    doclets = {
        "wait": wait
    }
    if doclet not in doclets:
        raise Errors.NO_DOCLET()
        return
    arguments = prompt[1:]
    result = doclets[doclet](arguments)
    return result
