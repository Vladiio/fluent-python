import reprlib, array, math, numbers, functools, operator, itertools


class Vector:
    typecode = 'd'
    components_shortcuts = 'xyzt'

    def __init__(self, components):
        self._components = array.array(self.typecode, components)

    def __len__(self):
        return len(self._components)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])

        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a

        return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __getattr__(self, name):
        if len(name) == 1:
            index = self.components_shortcuts.find(name)
            if 0 <= index < len(self._components):
                return self._components[index]
        cls = type(self)
        msg = 'type object {.__name__} has no attribute {!r}'.format(cls, name)
        raise AttributeError(msg)

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1 and name in self.components_shortcuts:
            msg = 'can\'t set attributes of type {.__name__!r}'
            raise TypeError(msg.format(cls))
        super().__setattr__(name, value)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self._components))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, self._components, 0)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        # import pdb
        # pdb.set_trace()
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
