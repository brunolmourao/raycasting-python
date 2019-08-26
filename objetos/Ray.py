"""""
Classe do Objeto Raio.
A classe Raio representa uma reta que tem inicio em P0 e direção dada pelo vetor n
Atributos:
    __p: Ponto
        Ponto que pertence a reta.
    __v_normal: Vetor
        Vetor Unitario que determina a direção da reta
"""


class Ray:
    # Método Construtor
    def __init__(self, p, v_normal):
        self.__p = p
        self.__v_normal = v_normal

    def ponto(self, t):
        return self.__p + t * self.__v_normal

    # Método getters
    @property
    def p(self):
        return self.__p

    @property
    def v_normal(self):
        return self.__v_normal
