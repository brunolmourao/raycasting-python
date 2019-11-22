import numpy as np

from DataStructure.Point import Point
from utils.Ray import Ray


class Sphere:
    def __init__(self, centro: Point, raio: float, material=None, cor=None):
        self.__centro = centro
        self.__raio = raio
        self.__material = material
        self.__cor = cor

    def intersection_with(self, reta: Ray):
        a = np.dot(reta.d, reta.d)
        b = np.dot(reta.p.coord - self.centro.coord, reta.d)
        c = np.dot(reta.p.coord - self.centro.coord, reta.p.coord - self.centro.coord) - self.raio ** 2

        delta = b ** 2 - a * c
        if delta >= 0:
            t = (-b + np.sqrt(delta)) / a
            t1 = (-b - np.sqrt(delta)) / a
            if t1 < t:
                t = t1
        else:
            t = None
        return t

    def transforme_coord_to_(self, c):
        centro_2D = np.append(self.centro.coord, 0)[:, np.newaxis]
        new_centro_2D = np.dot(c, centro_2D)
        new_centro_1D = new_centro_2D.transpose().squeeze()
        new_centro = np.delete(new_centro_1D, 3, 0)
        self.__centro = Point(new_centro[0], new_centro[1], new_centro[2])

    @property
    def centro(self):
        return self.__centro

    @property
    def raio(self):
        return self.__raio

    @property
    def material(self):
        return self.__material

    @property
    def cor(self):
        return self.__cor

    @material.setter
    def material(self, m):
        self.__material = m
