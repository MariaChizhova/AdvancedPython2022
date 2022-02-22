import numpy as np


class ArithmeticMixin(np.lib.mixins.NDArrayOperatorsMixin):
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        for inp in inputs:
            if not isinstance(inp, type(self)):
                return NotImplemented
        inputs = (inp.values for inp in inputs)
        return type(self)(getattr(ufunc, method)(*inputs, **kwargs))


class WriteToFileMixin:
    def write_to_file(self, path):
        with open(path, 'w') as file:
            file.write(str(self))


class StringMixin:
    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.values])

    def __repr__(self) -> str:
        return f'{type(self).__name__}({repr(self.values)})'


class GetSetMixin:
    def __init__(self, values):
        self.values = values

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        self._values = value


class MixinsMatrix(ArithmeticMixin, WriteToFileMixin, StringMixin, GetSetMixin):
    pass
