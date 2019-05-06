import sys
import random
from bisect import bisect, bisect_left, insort


HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_func):
    for needle in reversed(NEEDLES):
        position = bisect(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


def insort_demo():
    SIZE = 7
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE)
        insort(my_list, new_item)
        print('{:2d} -> {}'.format(new_item, my_list))


if __name__ == '__main__':
    bisect_func = bisect_left if sys.argv[-1] == 'left' else bisect
    # print('DEMO: {}'.format(bisect.__name__))
    # print('haystack ->',
        #   ' '.join(('{:2d}'.format(element) for element in HAYSTACK)))
    # demo(bisect_func)
    insort_demo()
