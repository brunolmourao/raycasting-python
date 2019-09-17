class Material:
    def __init__(self, m, ka, kd, ks):
        self.__k_amb = ka
        self.__k_dif = kd
        self.__k_spec = ks
        self.__m = m
