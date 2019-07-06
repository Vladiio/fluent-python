import functools
import time


DEFAULT_FMT = '[{elapsed_time:.5f}s] {name}({args_str}, {kwargs_str}) -> {result}'

def examine(format_template=DEFAULT_FMT):
    def _examine(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            started = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = time.perf_counter() - started
            name = func.__name__
            args_str = ','.join(str(arg) for arg in args)
            kwargs_str = ','.join((f'{key}={value}' for key, value in kwargs.items()))
            print(format_template.format(**locals()))
            return result
        return wrapper
    return _examine


@examine()
def work(b, a):
    for _ in range(10000):
        pass
    return 'Hello'

@examine('{name}: {elapsed_time}s')
def snooze(sec):
    time.sleep(sec)



@examine()
def factorial(n):
    return n if n == 1 else n * factorial(n - 1)


@examine()
def fib(n):
    first, second = 0, 1
    while (second < n):
       first, second = second, first + second
       print(first)


@functools.lru_cache()
@examine()
def fib2(n):
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)




if __name__ == '__main__':
    work(1, a=2)
    # print(factorial(5))
    # fib2(10)

