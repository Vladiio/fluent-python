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
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self._items)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """Return discount as a position dollar amount"""


class FidelityPromo(Promotion):

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0



class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        for item in order._items:
            discount += item.total() * .1 if item.quantity >= 20 else 0
        return discount


class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order):
        distinct_items = {item.product for item in order._items}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

