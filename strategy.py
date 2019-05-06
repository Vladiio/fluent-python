from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:
    def __init__(self, customer, items, promotion=None):
        self.customer = customer
        self._items = list(items)
        self.promotion = promotion


    def total(self):
        if not hasattr(self, __total):
            self.__total = sum(item.total() for item in self._items)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:2f} due: {:2f}>'
        return fmt.format(self.total(), self.due())

