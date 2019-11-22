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
        ppl_2D = np.append(self.ppl.coord, 0)[:, np.newaxis]
        new_ppl_2D = np.dot(c, ppl_2D)
        new_ppl_1D = new_ppl_2D.transpose().squeeze()
        new_ppl = np.delete(new_ppl_1D, 3, 0)
        self.__ppl = Point(new_ppl[0], new_ppl[1], new_ppl[2])

        n_2D = np.append(self.n, 1)[:, np.newaxis]
        new_n_2D = np.dot(c, n_2D)
        new_n_1D = new_n_2D.transpose().squeeze()
        new_n = np.delete(new_n_1D, 3, 0)
        self.__n = new_n

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
