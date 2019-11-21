import numpy as np

from DataStructure.Point import Point
from utils.Ray import Ray


class Cylinder:
    def __init__(self, centro: Point, vetor, raio, altura, material=None, cor=None):
        self.__centro = centro
        self.__u = vetor / np.linalg.norm(vetor)
        self.__raio = raio
        self.__altura = altura
        self.__material = material
        self.__cor = cor

    def intersection_with(self, reta: Ray):
        w = reta.d - np.dot(reta.d, self.u) * self.u
        v = (reta.p.coord - self.centro.coord) - (np.dot(reta.p.coord - self.centro.coord, self.u)) * self.u
        a = np.dot(w, w)
        b = np.dot(v, w)
        c = np.dot(v, v) - self.raio ** 2
        # print("u ", self.u)
        # print("a, b, c: ", a, b, c)

        delta = b ** 2 - a * c
        if delta >= 0:
            t = (-b + np.sqrt(delta)) / a
            t1 = (-b - np.sqrt(delta)) / a

            if t1 < t:
                t = t1
            p = reta.get_point(t).coord
            if 0 <= np.dot(p - self.centro.coord, self.u) <= self.altura:
                return t
        else:
            return None

    def transforme_coord_to_(self, c):
        centro_2D = np.append(self.centro.coord, 0)[:, np.newaxis]
        new_centro_2D = np.dot(c, centro_2D)
        new_centro_1D = new_centro_2D.transpose().squeeze()
        new_centro = np.delete(new_centro_1D, 3, 0)
        self.__centro = Point(new_centro[0], new_centro[1], new_centro[2])

        u_2D = np.append(self.u, 1)[:, np.newaxis]
        new_u_2D = np.dot(c, u_2D)
        new_u_1D = new_u_2D.transpose().squeeze()
        new_u = np.delete(new_u_1D, 3, 0)
        self.__u = new_u

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

    @property
    def material(self):
        return self.__material

    @property
    def cor(self):
        return self.__cor
