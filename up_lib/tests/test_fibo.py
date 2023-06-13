from up_lib.fibo import fib


def test_zero():
    assert fib(0) == 0


def test_one():
    assert fib(1) == 1


def test_five():
    assert fib(5) == 5


def test_twenty():
    assert fib(10) == 55


def test_slow():
    assert fib(333) == 1751455877444438095408940282208383549115781784912085789506677971125378
