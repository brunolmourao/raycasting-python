""""
Classe define um objeto Cilindro Reto.
Atributos:
    centro_base: Ponto
        Ponto com as coordenadas do centro da base
    raio: float
        Tamanho do raio da base do cilindro
    altura: float
        Altura do cilindro
    v_direcao: Vetor
        Vetor unitário que define a direção do eixo do cilindro
"""


class Cillinder:
    # Método Construtor
    def __init__(self, centro_base, raio, altura, v_direcao):
        self.__centro_base = centro_base
        self.__raio = raio
        self.__altura = altura
        self.__v_direcao = v_direcao

    # TODO: implementar equação do clindro
    @staticmethod
    def contem(t):
        """equação do ciclindro"""
        """t: float.
                t aplicado na equação gera o ponto 
        """

    # TODO: implementar equação de interseção com a reta
    @staticmethod
    def intersection_with(self, reta):
        """retona os t's dos pontos, se exitirem,
        caso nao existam retorna 0.

        """
        t1 = 0
        t2 = 0
        return t1, t2

    # Método getters
    @property
    def centro_base(self):
        return self.__centro_base

    @property
    def raio(self):
        return self.__raio

    @property
    def altura(self):
        return self.__altura

    @property
    def v_direcao(self):
        return self.__v_direcao
