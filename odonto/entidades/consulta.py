class Consulta():
    def __init__(self, paciente, data="", agendamento=""):
        self.__paciente = paciente
        self.__data = data
        self.__agendamento = agendamento


    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def agendamento(self):
        return self.__agendamento

    @agendamento.setter
    def data(self, agendamento):
        self.__agendamento = agendamento
