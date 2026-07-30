class OrdemServico:
    def __init__(self,
                 id_equipamento,
                 data_abertura,
                 defeito_relatado,
                 diagnostico,
                 solucao,
                 status,
                 prioridade,
                 valor_servico,
                 valor_pecas,
                 desconto,
                 valor_total,
                 observacoes,
                 id_ordem=None):

        self.__id_ordem = id_ordem
        self.__id_equipamento = id_equipamento
        self.__data_abertura = data_abertura
        self.__defeito_relatado = defeito_relatado
        self.__diagnostico = diagnostico
        self.__solucao = solucao
        self.__status = status
        self.__prioridade = prioridade
        self.__valor_servico = valor_servico
        self.__valor_pecas = valor_pecas
        self.__desconto = desconto
        self.__valor_total = valor_total
        self.__observacoes = observacoes

    def get_id_ordem(self):
        return self.__id_ordem

    def set_id_ordem(self, id_ordem):
        self.__id_ordem = id_ordem

    def get_id_equipamento(self):
        return self.__id_equipamento

    def get_data_abertura(self):
        return self.__data_abertura

    def get_defeito_relatado(self):
        return self.__defeito_relatado

    def get_diagnostico(self):
        return self.__diagnostico

    def get_solucao(self):
        return self.__solucao

    def get_status(self):
        return self.__status

    def get_prioridade(self):
        return self.__prioridade

    def get_valor_servico(self):
        return self.__valor_servico

    def get_valor_pecas(self):
        return self.__valor_pecas

    def get_desconto(self):
        return self.__desconto

    def get_valor_total(self):
        return self.__valor_total

    def get_observacoes(self):
        return self.__observacoes