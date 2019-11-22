import numpy as np

from DataStructure.Edge import Edge
from DataStructure.Point import Point


def normal_vector(p1, p2, p3):
    v1 = p2.coord - p1.coord
    v2 = p3.coord - p1.coord
    nv = np.cross(v1, v2)
    return nv / np.linalg.norm(nv)


class Face:
    def __init__(self, vertice1: Point, vertice2: Point, vertice3: Point):
        self.__a1 = Edge(vertice1, vertice2)
        self.__a2 = Edge(vertice2, vertice3)
        self.__a3 = Edge(vertice3, vertice1)
        self.__p1 = vertice1
        self.__p2 = vertice2
        self.__p3 = vertice3
        self.__label = vertice1.label + vertice2.label + vertice3.label
        self.__normal_vector = normal_vector(vertice1, vertice2, vertice3)

    @property
    def a1(self):
        return self.__a1

    @property
    def a2(self):
        return self.__a2

    @property
    def a3(self):
        return self.__a3

    @property
    def p1(self):
        return self.__p1

    @property
    def p2(self):
        return self.__p2

    @property
    def p3(self):
        return self.__p3

    @property
    def normal_vector(self):
        return self.__normal_vector

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l
