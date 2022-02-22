class MulMixin:
    """
      Hash function = sum of elements divided by prime number 10^9+7
    """

    def __hash__(self):
        return sum(map(sum, self.values)) % (10 ** 9 + 7)


class Matrix(MulMixin):
    def __init__(self, values):
        values = list(values)
        self.values = []
        for row in values:
            if len(row) != len(values[0]):
                raise ValueError("Rows should have equal sizes")
            self.values.append(list(row))
        self.n = len(self.values)
        self.m = len(self.values[0])
        self._mul_cache = {}

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError(f"Matrix sizes should be the same. Actual: [{self.n}x{self.m}] and [{other.n}x{other.m}]")
        return Matrix(
            [elem1 + elem2 for elem1, elem2 in zip(row1, row2)] for row1, row2 in zip(self.values, other.values))

    def __mul__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError(f"Matrix sizes should be the same. Actual: [{self.n}x{self.m}] and [{other.n}x{other.m}]")
        return Matrix(
            [elem1 * elem2 for elem1, elem2 in zip(row1, row2)] for row1, row2 in zip(self.values, other.values))

    def __matmul__(self, other):
        if self.m != other.n:
            raise ValueError(f"Matrix sizes should be the same. Actual: [{self.n}x{self.m}] and [{other.n}x{other.m}]")
        key = self.__hash__(), other.__hash__()
        if key in self._mul_cache:
            return self._mul_cache[key]
        res = Matrix(
            [[sum([self.values[i][k] * other.values[k][j] for k in range(self.m)]) for j in range(other.m)] for i in
             range(self.n)])
        self._mul_cache[key] = res
        return res

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.values])
