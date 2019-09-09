import numpy as np
import utils.CalcWithVectors as calc


class Light:
    # Inicia a Luz com um Atributo rgb que é um array com os valores RGB, entre 0 e 1
    def __init__(self, rgb):
        self.__rgb = rgb
        # Calcula o vetor resultante da interação da Luz com o material do objeto

    def arroba(self, prop_obj):
        result = []
        for x in range(3):
            result.append(self.__rgb[x] * prop_obj[x])
        return result


# Luz Ambiente herda os atributos de Light
class EnvironmentLight(Light):
    def __init__(self, rgb):
        super().__init__(rgb)

    def iluminar(self, prop_obj):
        return super().arroba(prop_obj)


class PointLight(Light):
    # Onde ppnt é o Ponto de onde a luz pontual é gerada
    def __init__(self, rgb, ppont):
        super().__init__(rgb)
        self.__ppont = ppont

    # TODO Calcular n
    def iluminar(self, prop_obj, n, p0, pint):
        l = p0 - pint / calc.norma(p0 - pint)
        fd = calc.produto_escalar(n, l)
        if fd < 0:
            fd = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fd
        return product
