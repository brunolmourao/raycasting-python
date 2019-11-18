import numpy as np

from DataStructure.Point import Point
from utils.Ray import Ray


class Cylinder:
    def __init__(self, centro: Point, vetor, raio, altura, material=None):
        self.__centro = centro.coord
        self.__u = vetor / np.linalg.norm(vetor)
        self.__raio = raio
        self.__altura = altura
        self.__material = material

    def intersection_with(self, reta: Ray):
        w = reta.d - np.dot(reta.d, self.u) * self.u
        v = (reta.p.coord - self.centro) - (np.dot(reta.p.coord - self.centro, self.u)) * self.u
        a = np.dot(w, w)
        b = np.dot(v, w)
        c = np.dot(v, v) - self.raio ** 2
        # print("u ", self.u)
        # print("a, b, c: ", a, b, c)

        delta = b ** 2 - a * c
        if delta >= 0:
            t = (-b + np.sqrt(delta)) / a
            t1 = (-b - np.sqrt(delta)) / a

            #  print("delta ", delta)
            # print("t ", t, reta.get_point(t).coord)
            # print("t1", t1, reta.get_point(t1).coord)

            if t1 < t:
                t = t1
            p = reta.get_point(t).coord
            # print("p", p)
            # print(np.dot(p - self.centro, self.u))
            if 0 <= np.dot(p - self.centro, self.u) <= self.altura:
                return t
        else:
            return None

    @property
    def centro(self):
        return self.__centro

    @property
    def u(self):
        return self.__u

    @property
    def raio(self):
        return self.__raio

    @property
    def altura(self):
        return self.__altura
