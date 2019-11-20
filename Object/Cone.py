import numpy as np

from DataStructure.Point import Point
from utils.Ray import Ray


class Cone:
    def __init__(self, centro: Point, vetor, raio, altura, material=None, cor=None):
        self.__centro = centro
        self.__raio = raio
        self.__altura = altura
        self.__n = vetor / np.linalg.norm(vetor)
        self.__material = material
        self.__cor = cor

    def intersection_with(self, reta: Ray):
        V = self.centro.coord + self.n * self.altura

        v = V - reta.p.coord
        n = self.n
        d = reta.d
        cos_theta = self.altura / np.sqrt(pow(self.raio, 2) + pow(self.altura, 2))

        a = np.power(np.dot(d, n), 2) - np.dot(d, d) * np.power(cos_theta, 2)
        b = np.dot(v, d) * np.power(cos_theta, 2) - np.dot(v, n) * np.dot(d, n)
        c = np.power(np.dot(v, n), 2) - np.dot(v, v) * np.power(cos_theta, 2)

        if a == 0:
            print("nao era pra ser")
        delta = b ** 2 - a * c
        if delta >= 0:
            t = -b + np.sqrt(delta) / a
            t1 = -b - np.sqrt(delta) / a

            if t1 < t:
                t = t1

            vp = V - reta.get_point(t).coord
            return t

            if 0 <= np.dot(vp, n) <= self.altura:
                return t
            else:
                return None

        else:
            return None

    def transforme_coord_to_(self, c):
        pass

    @property
    def centro(self):
        return self.__centro

    @property
    def raio(self):
        return self.__raio

    @property
    def altura(self):
        return self.__altura

    @property
    def n(self):
        return self.__n

    @property
    def material(self):
        return self.__material

    @property
    def cor(self):
        return self.__cor
