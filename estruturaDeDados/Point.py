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
