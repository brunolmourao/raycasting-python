"""""
Classe do Objeto Raio.
A classe Raio representa uma reta que tem inicio em P0 e direção dada pelo vetor n
Atributos:
    __p: Ponto
        Ponto que pertence a reta.
    __v_normal: Vetor
        Vetor Unitario que determina a direção da reta
"""
import numpy as np


class Ray:
    # Método Construtor
    def __init__(self, p, v_normal):
        self.__p = np.array(p)
        self.__v_direcao = np.array(v_normal)

    # TODO verificar se essas operações estao adequadas para a estrutura de dados
    # que vamos usar
    def ponto(self, t):
        return self.__p + t * self.__v_direcao

    # Método getters
    @property
    def p(self):
        return self.__p

    @property
    def v_normal(self):
        return self.__v_direcao
