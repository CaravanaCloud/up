from up_lib.action.wait import wait
from timeit import default_timer as timer


def test_simple_wait():
    start = timer()
    wait({}, ["sleep", "2"])
    end = timer()
    elapsed = end - start
    assert elapsed > 2.0

