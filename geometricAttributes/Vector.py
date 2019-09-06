import numpy as np
from objetos.Point import Point


class Vector:

    def __init__(self, origem: Point, destino: Point):
        pass

    def norma(self):
        return np.sqrt(np.power(self.__x, 2) + np.power(self.__y, 2) + np.power(self.__z, 2))

    def auto_normalizar(self):
        n = self.norma()
        if n > 0:
            return Point(self.__x / n, self.__y / n, self.__z / n)
