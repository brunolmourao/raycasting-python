import numpy as np

from DataStructure.Point import Point


class Ray:
    def __init__(self, p: Point, d):
        self.__p = p
        self.__d = d / np.linalg.norm(d)

    def get_point(self, t: float):
        if t is None:
            return False
        else:
            v = self.p.coord + t * self.d
            return Point(v[0], v[1], v[2])

    @property
    def p(self):
        return self.__p

    @property
    def d(self):
        return self.__d
