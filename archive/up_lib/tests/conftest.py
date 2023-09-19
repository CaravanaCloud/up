from up_lib.loader import load_plugins
from up_lib.log import *


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    init_logging()
    print("Test logging configured in test session")
    load_plugins()
    print("Plugins loaded in test session")