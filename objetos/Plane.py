""""
Classe do Objeto Plano
Atributos
    ppl: Ponto
        Um ponto qualquer pertecente ao plano;
    v_normal: Vetor
        Vetor unitário perpendicular ao plano.
"""
from auxiliar.CalcWithVectors import produto_escalar


class Plane:
    # Método Construtor
    def __init__(self, ppl, v_normal):
        self.__p = ppl
        self.__v_normal = v_normal

    # TODO: implementar equação do plano
    @staticmethod
    def ponto(t):
        """equação do plano"""
        """t: float.
                t aplicado na equação gera o ponto 
        """

    # TODO: terminar de implementar
    def intersection_with(self, reta):
        """ Verifica inicialmente se a reta e o plano não são parelelos
            (u.n != 0), caso sejam retorna false, caso contrário retorna t"""
        prod_esc_un = produto_escalar(reta.v_normal, self.v_normal)
        if prod_esc_un:
            t = produto_escalar(self.__p - reta.p, self.__v_normal) / prod_esc_un
            return t
        else:
            return False

    # Método getters
    @property
    def ppl(self):
        return self.__p

    @property
    def v_normal(self):
        return self.__v_normal