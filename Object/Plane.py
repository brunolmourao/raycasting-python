import numpy as np

from DataStructure.Point import Point
from utils.Ray import Ray


class Plane:
    def __init__(self, p: Point, n, material=None, cor=None):
        self.__ppl = p
        self.__n = n / np.linalg.norm(n)
        self.__material = material
        self.__cor = cor

    def intersection_with(self, r: Ray):
        if np.dot(r.d, self.n):
            return np.dot(self.ppl.coord - r.p.coord, self.n) \
                   / np.dot(r.d, self.n)
        return None

    def transforme_coord_to_(self, c):
        pass

    @property
    def n(self):
        return self.__n

    @property
    def ppl(self):
        return self.__ppl

    @property
    def material(self):
        return self.__material

    @property
    def cor(self):
        return self.__cor
