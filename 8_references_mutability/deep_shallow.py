import copy


class Bus:
    def __init__(self, passengers=None):
        self.passengers = [] if passengers is None else list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

class HauntedBus(Bus):
    def __init__(self, passengers=[]):
        """
            Default parameter values are created only once during method definition.
            If we assign a mutable object as a default we'll end up dealing with the
            same entity across different instances
        """
        self.passengers = passengers

class TwilightBus(Bus):
    def __init__(self, passengers=None):
        """
            The issue here is that when a caller provides a mutable object
            it'll be mutated outside the class as self.passengers and passengers are just aliases
        """
       self.passengers = [] if passengers is None else passenger


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)


