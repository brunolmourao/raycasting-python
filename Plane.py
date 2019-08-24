""""
Classe do Objeto Plano
A classe Plane representa um plano onde:
p é um	ponto qualquer do plano;
ppl é um ponto específico (conhecido) do plano; e
vet_n é	o vetor	unitário perpendicular ao plano, isto é, a todos os	vetores paralelos ao plano.
"""


class Plane:
    # Método Construtor
    def __init__(self, p, ppl, vet_n):
        self.__p = p
        self.__ppl = ppl
        self.__vet_n = vet_n

    # Método getters
    @property
    def p(self):
        return self.__p

    @property
    def ppl(self):
        return self.__ppl

    @property
    def vet_n(self):
        return self.__vet_n
