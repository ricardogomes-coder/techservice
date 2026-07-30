class Cliente:
    def __init__(self, nome, email, telefone, nif=None, morada=None, id_cliente=None):
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__nif = nif
        self.__morada = morada
        self.__status = 1
        self.__data_cadastro = None
        self.__data_alteracao = None
        self.__data_eliminacao = None

    def get_id_cliente(self):
        return self.__id_cliente

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_telefone(self):
        return self.__telefone

    def get_nif(self):
        return self.__nif

    def get_morada(self):
        return self.__morada

    def get_status(self):
        return self.__status

    def get_data_cadastro(self):
        return self.__data_cadastro

    def get_data_alteracao(self):
        return self.__data_alteracao

    def get_data_eliminacao(self):
        return self.__data_eliminacao
