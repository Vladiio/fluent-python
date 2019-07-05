import functools
from time import perf_counter



def examine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        started = perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = perf_counter() - started
        args_str = ','.join(str(arg) for arg in args)
        kwargs_str = ','.join((f'{key}={value}' for key, value in kwargs.items()))
        print(f'[{elapsed_time:.5f}s] {func.__name__}({args_str}, {kwargs_str}) -> {result}')
        return result
    return wrapper


@examine
def work(b, a):
    for _ in range(10000):
        pass
    return 'Hello'


@examine
def factorial(n):
    return n if n == 1 else n * factorial(n - 1)


@examine
def fib(n):
    first, second = 0, 1
    while (second < n):
       first, second = second, first + second
       print(first)


@examine
def fib2(n):
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)


if __name__ == '__main__':
    # work(1, a=2)
    # print(factorial(5))
    fib2(10)

