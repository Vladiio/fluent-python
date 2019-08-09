import contextlib


class LookingGlass:

    def custom_stdout_write(self, data):
        self.original_stdout_write(data[::-1])

    def __enter__(self):
        import sys
        self.original_stdout_write = sys.stdout.write
        sys.stdout.write = self.custom_stdout_write
        return 'GLASS'

    def __exit__(self, err_type, err_value, traceback):
        import sys
        sys.stdout.write = self.original_stdout_write
        if err_type:
            return True


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write

    try:
        yield 'ABC'
    except TypeError:
        print('error')
    finally:
        sys.stdout.write = original_write
