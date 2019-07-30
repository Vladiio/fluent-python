import collections

Card = collections.namedtuple('Card', ('rank', 'suit'))


class FrenchDeck(collections.abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.ranks for suit in self.suits]

    def __setitem__(self, position, value):
        self._cards[position] = card

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)

    def __getitem__(self, index):
        return self._cards[index]

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        return 'Deck'


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_hich(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
