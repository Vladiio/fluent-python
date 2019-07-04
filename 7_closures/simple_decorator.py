from time import time


def examine(func):
    def wrapper(*args, **kwargs):
        started_at = time()
        result = func(*args, **kwargs)
        elapsed_time = time() - started_at
        print(f'It took {elapsed_time}ms to execute {func.__name__}')
        kwargs_str = ','.join((f'{key}={value}' for key, value in kwargs.items()))
        print(f'Arguments: {args}, Keyword arguments: {kwargs_str}, result: {result}')
        return result
    return wrapper

@examine
def work(b, a):
    for _ in range(10000):
        pass
    return 'Hello'


work(1, a=2)
