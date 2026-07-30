class Cliente:

    
    class Cliente:
        def __init__(self, nome, email, telefone, nif=None, morada=None):
            self.id_cliente = None
            self.nome = nome
            self.email = email
            self.telefone = telefone
            self.nif = nif
            self.morada = morada
            self.status = 1

    def adicionar(self):
        from src.repositories import cliente_repository
        return cliente_repository.inserir(self)