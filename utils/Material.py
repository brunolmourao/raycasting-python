class Material:
    def __init__(self, mat_dif, mat_sp, mat_amb):
        self.__mat_dif = mat_dif
        self.__mat_sp = mat_sp
        self.__mat_amb = mat_amb

    @property
    def mat_dif(self):
        return self.__mat_dif

    @property
    def mat_sp(self):
        return self.__mat_sp

    @property
    def mat_amb(self):
        return self.__mat_amb
