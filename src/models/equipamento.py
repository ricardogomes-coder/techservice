class Equipamento:
    def __init__(self, id_cliente, tipo, marca, modelo,
                 numero_serie, data_compra, observacoes,
                 id_equipamento=None):

        self.__id_equipamento = id_equipamento
        self.__id_cliente = id_cliente
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo
        self.__numero_serie = numero_serie
        self.__data_compra = data_compra
        self.__observacoes = observacoes

    def get_id_equipamento(self):
        return self.__id_equipamento

    def set_id_equipamento(self, id_equipamento):
        self.__id_equipamento = id_equipamento

    def get_id_cliente(self):
        return self.__id_cliente

    def get_tipo(self):
        return self.__tipo

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_numero_serie(self):
        return self.__numero_serie

    def get_data_compra(self):
        return self.__data_compra

    def get_observacoes(self):
        return self.__observacoes