import abc, random


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise 'LookupError' when the instance is empty.
        """

    def loaded(self):
        """Return 'True' if there's at least 1 item, 'False' otherwise."""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                item = self.pick()
                items.append(item)
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):

    def __init__(self, items):
        self._items = []
        self._randomizer = random.SystemRandom()
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __cal__(self):
        self.pick()


class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)
        self._randomizer = random.SystemRandom()

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            self._randomizer.choice(self._balls)
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def inspect(self):
        return tuple(sorted(self._balls))

    def loaded(self):
        return bool(self._balls)


@Tombola.register
class TomboList(list):

    def load(self):
        pass

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


