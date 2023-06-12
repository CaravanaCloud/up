from up_lib.command import Command
from up_lib.wait import wait
from timeit import default_timer as timer


def test_simple_wait():
    start = timer()
    cmd = Command(("wait",), {}, ["sleep", "2"])
    wait(cmd)
    end = timer()
    elapsed = end - start
    assert elapsed > 2.0

