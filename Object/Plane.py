import numpy as np

from DataStructure.Point import Point
from utils.Ray import Ray


class Plane:
    def __init__(self, p: Point, n):
        self.__ppl = p
        self.__n = n / np.linalg.norm(n)

    def intersection_with(self, r: Ray):
        if np.dot(r.d, self.n):
            return np.dot(self.ppl.coord - r.p.coord, self.n) \
                   / np.dot(r.d, self.n)
        return None

    @property
    def n(self):
        return self.__n

    @property
    def ppl(self):
        return self.__ppl
