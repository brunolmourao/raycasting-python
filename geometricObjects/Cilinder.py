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
from utils.CalcWithVectors import produto_escalar
from utils.QuadraticOperations import roots


class Cillinder:

    def __init__(self, centro_base, raio, altura, v_direcao):
        self.__centro_base = centro_base.coords()
        self.__raio = raio
        self.__altura = altura
        self.__v_direcao = v_direcao.coords()
        self.cor = ""

    def intersection_with(self, reta):
        pb = reta.p.coords() - self.__centro_base
        d = reta.v_direcao
        w = self.calc_coefficien(d)
        v = self.calc_coefficien(pb)

        a = produto_escalar(w, w)
        b = 2 * produto_escalar(v, w)
        c = produto_escalar(v, v) - self.__raio * self.__raio
        tint = []
        root = roots(a, b, c)

        # TODO corrigir comportamento da validação
        # print(f" tint: {len(tint)}", end=" ")
        # if len(tint) == 0:
        #    print("")
        index = 0
        for x in root:
            p0b = reta.ponto(x).coords() - self.centro_base
            u = self.v_direcao
            if (produto_escalar(p0b, u) >= 0) and (produto_escalar(p0b, u) < self.altura):
                print(f"x = {x}")
                tint.append(x)
            # print(f"Roots {root}, tint = {tint}")
        return root

    def calc_coefficien(self, coe):
        return coe - produto_escalar(coe, self.v_direcao) * self.v_direcao

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

    # Métodos setter
    @centro_base.setter
    def centro_base(self, v):
        self.centro_base = v

    @v_direcao.setter
    def v_direcao(self, v):
        self.__v_direcao = v

    @altura.setter
    def altura(self, a):
        self.__altura = a

    @raio.setter
    def raio(self, r):
        self.__raio = r

    def set_cor(self, c):
        self.cor = c

    """
        @staticmethod
        def ponto(self, t):
            rq = produto_escalar(self.__raio, self.__raio)
            sub = Ray.ponto(t) - self.__centro_base
            prod_esc_sub = produto_escalar(sub, self.__v_direcao)
            vet_norm = sub - produto_escalar(prod_esc_sub, self.__v_direcao)
            result = produto_escalar(norma(vet_norm), norma(vet_norm))
            if result == rq and 0 <= prod_esc_sub <= self.__altura:
                return True
            else:
                return False
    """
