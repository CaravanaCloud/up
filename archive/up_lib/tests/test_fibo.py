from up_lib.cmd.fibo import fib
from up_lib.main import up

def test_zero():
    assert fib(0) == 0


def test_one():
    assert fib(1) == 1


def test_five():
    assert fib(5) == 5


def test_twenty():
    assert fib(10) == 55


def test_bigone():
    assert str(fib(500000))[0:10] == "2955561408" 


def test_waiter_simple():
    result = up(line="wait: fibo --x=10", context={})
    assert result["y"] == 55

def test_waiter_timeout():
    pass #TODO actually timeout internal and external commands