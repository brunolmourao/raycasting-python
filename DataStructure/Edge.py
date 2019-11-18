from DataStructure import Point


class Edge:
    def __init__(self, p1: Point, p2: Point):
        self.__p1 = p1
        self.__p2 = p2
        self.__label = p1.label + p2.label

    @property
    def s(self):
        return self.__p1

    @property
    def d(self):
        return self.__p2

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l
