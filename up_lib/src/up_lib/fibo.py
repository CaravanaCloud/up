from .log import *

def fib(x: int) -> int:
    ## TODO: Input reflection
    return up_fibo({"x": x}).get("result", -1)


def up_fibo(opts:dict) -> dict:
    x: int = int(opts.get("x", 0))
    debug("Calculating fib(%s)", x)
    if x <= 1:
        return {"result": x}

    a, b = 0, 1
    for _ in range(2, x + 1):
        a, b = b, a + b

    return {"result": b}
