import itertools

# a more pythonic way would be to implement a generator function
class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or current < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def aitprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    gen = itertools.count(first, step)
    if end is not None:
        gen = itertools.takewhile(lambda n: n < end, gen)

    return gen


