import numpy as np
from estruturaDeDados.Point import Point


class Vector:
    # Gera o vetor com as coordenadas
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def norma(self):
        return np.sqrt(np.power(self.__x, 2) + np.power(self.__y, 2) + np.power(self.__z, 2))

    def auto_normalizar(self):
        n = self.norma()
        if n > 0:
            return Vector(self.__x / n, self.__y / n, self.__z / n)