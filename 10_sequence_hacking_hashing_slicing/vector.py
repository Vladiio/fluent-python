import reprlib
import array
import math


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array.array(self.typecode, components)

    def __len__(self):
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)



