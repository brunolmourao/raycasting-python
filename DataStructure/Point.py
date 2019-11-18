import numpy as np


class Point:
    def __init__(self, x, y, z, label=""):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__label = label
        self.__coord = np.array([x, y, z])

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @property
    def label(self):
        return self.__label

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, c):
        self.__coord = c

    @label.setter
    def label(self, l):
        self.__label = l
