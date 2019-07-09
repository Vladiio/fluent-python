import sys
import resource
import importlib

NUM_VECTORS = 10 ** 7

if len(sys.argv) == 2:
    module_name = sys.argv[1].replace('.py', '')
    module = importlib.import_module(module_name)
else:
    print('Usage: {} <vector-module-to-test>'.format())
    sys.exit(1)


def main(class_name):
    print(f'Selected vector type:{module.__name__}.{module.Vector2d.__name__}')
    print(f'Creating {NUM_VECTORS:,} vector instances')

    ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f'Initial RAM usage: {ram:14,}')
    v = [module.Vector2d(3, 4) for _ in range(NUM_VECTORS)]
    ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f'Final RAM usage: {ram:14,}')



if __name__ == '__main__':
    main(sys.argv[-1])
