class Dependente():
    def __init__(self, paciente, nome, nascimento, tipo):
        self.__paciente = paciente
        self.__nome = nome
        self.__nascimento = nascimento
        self.__tipo = tipo

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def dono(self, paciente):
        self.__paciente = paciente

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def categoria(self, tipo):
        self.__tipo = tipo

