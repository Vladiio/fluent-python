import weakref


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f'Cheese({self.kind})'


stock = weakref.WeakValueDictionary()
catalog = [Cheese(kind) for kind in ('Red Leicester', 'Tilsit', 'Brie', 'Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

del catalog
print(sorted(stock.keys()))

del cheese
print(sorted(stock.keys()))
