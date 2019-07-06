registry = set()

def register(active=True):
    def _register(func):
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return _register

@register()
def f1():
    print('running f1')

@register(active=False)
def f2():
    print('running f2')

print(registry)
