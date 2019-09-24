class Material:
    def __init__(self, m, ka, kd, ks):
        self.__k_amb = ka
        self.__k_dif = kd
        self.__k_spec = ks
        self.__m = m

    def ka(self):
        return self.__k_amb
    def kd(self):
        return self.__k_dif
    def ks(self):
        return self.__k_spec