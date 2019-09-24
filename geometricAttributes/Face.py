"""
Classe que representa uma face triangular a ser usava para realizar intersecções
"""


class Face:
    def __init__(self, i, p1, p2, p3):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__id = i

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
    def id(self):
        return self.__id
