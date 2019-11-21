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

        delta = b ** 2 - a * c
        if a != 0 and delta >= 0:
            t = (-b + np.sqrt(delta)) / a
            vp = V - reta.get_point(t).coord
            if t < 0: return None
            if 0 <= np.dot(vp, n) <= self.altura:
                return t
            else:
                return None
        else:
            return None

    def transforme_coord_to_(self, c):
        # print("teste ====================")
        # print("antes: ", self.centro.coord, self.centro.coord.shape)

        centro_2D = np.append(self.centro.coord, 0)[:, np.newaxis]
        new_centro_2D = np.dot(c, centro_2D)
        new_centro_1D = new_centro_2D.transpose().squeeze()
        new_centro = np.delete(new_centro_1D, 3, 0)
        self.__centro = Point(new_centro[0], new_centro[1], new_centro[2])

        n_2D = np.append(self.n, 1)[:, np.newaxis]
        new_n_2D = np.dot(c, n_2D)
        new_n_1D = new_n_2D.transpose().squeeze()
        new_n = np.delete(new_n_1D, 3, 0)
        self.__n = new_n

        # print(f"{centro_2D} {np.shape(centro_2D)}")
        # print(f"{new_centro_2D} {new_centro_2D.shape}")
        # print(f"{new_centro_1D} {np.shape(new_centro_1D)}")
        # print(f"{new_centro} {np.shape(new_centro)}")
        # print("n")
        # print(f"{n_2D} {np.shape(n_2D)}")
        # print(f"{new_n_2D} {new_n_2D.shape}")
        # print(f"{new_n_1D} {np.shape(new_n_1D)}")
        # print(f"{new_n} {np.shape(new_n)}")

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
