"""
Classe que calcula operações básicas para os problemas, como delta, normalização, dentre outras

"""


class QuadraticOperations:

    @staticmethod
    def delta(a, b, c):
        return b * b - 4 * a * c

    @staticmethod
    def roots(a, b, c):
        d = QuadraticOperations.delta(a, b, c)
        if d < 0:
            return
        elif d == 0:
            return (-1) * b / 2 * a
        else:
            return [((-1) * b + QuadraticOperations.delta(a, b, c) ** 0.5) / 2 * a,
                    ((-1) * b + QuadraticOperations.delta(a, b, c) ** 0.5) / 2 * a]
