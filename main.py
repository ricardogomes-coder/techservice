from src.models.cliente import Cliente
from src.repositories.cliente_repository import listar
from src.repositories.cliente_repository import adicionar
print(Cliente.__init__)
def main():
    print("=== TechService - Sistema de Gestão de Assistência Técnica ===")

    print("\n=== Novo Cliente ===")

    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    nif = input("NIF: ")
    morada = input("Morada: ")

    cliente = Cliente(
        nome=nome,
        email=email,
        telefone=telefone,
        nif=nif,
        morada=morada
    )

    adicionar(cliente)

    print("\nCliente inserido com sucesso!")
    print(f"ID: {cliente.get_id_cliente()}")
    print(f"Nome: {cliente.get_nome()}")
    print(f"Email: {cliente.get_email()}")
    print(f"Telefone: {cliente.get_telefone()}")
    print(f"NIF: {cliente.get_nif()}")
    print(f"Morada: {cliente.get_morada()}")


    # Listar clientes ativos
    print("\n=== Clientes ativos ===")

    clientes = listar()

    for item in clientes:
        print("--------------------")
        print(f"ID: {item['id_cliente']}")
        print(f"Nome: {item['nome']}")
        print(f"Email: {item['email']}")
        print(f"Telefone: {item['telefone']}")


if __name__ == "__main__":
    main()