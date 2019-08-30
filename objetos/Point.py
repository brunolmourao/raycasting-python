import numpy as np


class Point:

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def distancia(self, ponto):
        return np.sqrt(np.power(ponto.__x - self.__x, 2)
                       + np.power(ponto.__y - self.__y, 2)
                       + np.power(ponto.__z - self.__z, 2))

    def norma(self):
        return np.sqrt(np.power(self.__x, 2) + np.power(self.__y, 2) + np.power(self.__z, 2))

    def auto_normalizar(self):
        n = self.norma()
        if n > 0:
            return Ponto(self.__x / n, self.__y / n, self.__z / n)
