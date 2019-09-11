"""
Classe que representa uma face triangular a ser usava para realizar intersecções
"""


class Face:
    def __init__(self, p1, p2, p3,id):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__id = id
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