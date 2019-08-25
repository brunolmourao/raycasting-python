"""A classe Cube define um CUBO.
    Atributos
    centro_base: Ponto
        Um ponto com as coordenadas do centro da base
    aresta: float
        O tamanho da aresta do cubo
    v_direcao: Vetor
        Um vetor unitario que é a normal a base do cubo
"""


class Cube(object):
    def __init__(self, centro_base, aresta, v_direcao):
        self.__v_direcao = v_direcao
        self.__aresta = aresta
        self.__centro_base = centro_base

    # TODO: implementar a equação de interseção com a reta
    @staticmethod
    def intersection_with(self, reta):
        """retona os t's dos pontos, se exitirem,
        caso nao existam retorna 0.

        """
        t1 = 0
        t2 = 0
        return t1, t2
