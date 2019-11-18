import numpy as np

from DataStructure.Point import Point


class Vector:

    def __init__(self, source: Point, destiny: Point):
        self.__s = source
        self.__d = destiny
        self.__label = ""
        self.__coord = destiny.coord - source.coord

    def norm(self):
        return self.coord / np.linalg.norm(self.coord)

    @property
    def s(self):
        return self.__s

    @property
    def d(self):
        return self.__d

    @property
    def coord(self):
        return self.__coord

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l
