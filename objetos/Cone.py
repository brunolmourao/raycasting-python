"""
Classe define o objeto Cone Reto
Atributos:
    vertice: Ponto
        Vértice do cone;
    v_direcao: Vetor
        Vetor unitário que define a direção do eixo do cone;
    theta: float
        é o ângulo entre a geratriz	e o	eixo do	cone;
    altura: float
        A altura do	cone;
    raio: float
        Raio da base do cone.
"""


class Cone:
    __theta = 0

    # TODO: calculo de theta. Verificar se o que esta comentado esta correto
    # Método Construtor
    def __init__(self, vertice, v_direcao, altura, raio):
        self.__vertice = vertice
        self.__v_direcao = v_direcao
        self.__altura = altura
        self.__raio = raio
        # p_raio = [raio, 0, 0]
        # geratriz = vertice - p_raio
        # self.theta = altura/np.linalg.norm(geratriz)

    # TODO: implementar equação do clindro
    @staticmethod
    def contem(t):
        """equação do cone"""
        """t: float.
                t aplicado na equação gera o ponto 
        """

    # TODO: implementar a equação de interseção com a reta
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
    def vertice(self):
        return self.__vertice

    @property
    def v_direcao(self):
        return self.__v_direcao

    @property
    def altura(self):
        return self.__altura

    @property
    def theta(self):
        return self.__theta

    @property
    def raio(self):
        return self.__raio
