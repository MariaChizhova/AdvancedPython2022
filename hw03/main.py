import os
import numpy as np

from hw03.matrix import Matrix
from hw03.mixins_matrix import MixinsMatrix

if __name__ == '__main__':
    if not os.path.exists('artifacts'):
        os.mkdir('artifacts')
    if not os.path.exists('artifacts/easy'):
        os.mkdir('artifacts/easy')
    if not os.path.exists('artifacts/medium'):
        os.mkdir('artifacts/medium')
    if not os.path.exists('artifacts/hard'):
        os.mkdir('artifacts/hard')

    # easy task
    np.random.seed(0)
    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))
    with open('artifacts/easy/matrix+.txt', 'w') as file:
        file.write((m1 + m2).__str__())
    with open('artifacts/easy/matrix*.txt', 'w') as file:
        file.write((m1 * m2).__str__())
    with open('artifacts/easy/matrix@.txt', 'w') as file:
        file.write((m1 @ m2).__str__())

    # medium task
    m1 = MixinsMatrix(np.random.randint(0, 10, (10, 10)))
    m2 = MixinsMatrix(np.random.randint(0, 10, (10, 10)))
    (m1 + m2).write_to_file('artifacts/medium/matrix+.txt')
    (m1 * m2).write_to_file('artifacts/medium/matrix*.txt')
    (m1 @ m2).write_to_file('artifacts/medium/matrix@.txt')

    # hard task
    a = Matrix([[0, 0], [0, 0]])
    b = Matrix([[1, 0], [0, -1]])
    c = Matrix([[1, 0], [0, 1]])
    d = b
    with open('artifacts/hard/A.txt', 'w') as file:
        file.write(a.__str__())
    with open('artifacts/hard/B.txt', 'w') as file:
        file.write(b.__str__())
    with open('artifacts/hard/C.txt', 'w') as file:
        file.write(c.__str__())
    with open('artifacts/hard/D.txt', 'w') as file:
        file.write(d.__str__())

    with open('artifacts/hard/AB.txt', 'w') as file:
        file.write((a @ b).__str__())
    c._mul_cache = {}
    with open('artifacts/hard/CD.txt', 'w') as file:
        file.write((c @ d).__str__())
    with open('artifacts/hard/hash.txt', 'w') as file:
        file.write(f'Hash AB: {(a @ b).__hash__()}\n')
        file.write(f'Hash CD: {(c @ d).__hash__()}\n')
