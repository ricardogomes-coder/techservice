from src.models.cliente import Cliente
from src.repositories.cliente_repository import listar, adicionar, atualizar, eliminar


def inserir_cliente():
    print("\n=== Inserir Cliente ===")

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


def listar_clientes():
    print("\n=== Clientes ativos ===")

    clientes = listar()

    for item in clientes:
        print("--------------------")
        print(f"ID: {item['id_cliente']}")
        print(f"Nome: {item['nome']}")
        print(f"Email: {item['email']}")
        print(f"Telefone: {item['telefone']}")
        print(f"NIF: {item['nif']}")
        print(f"Morada: {item['morada']}")


def atualizar_cliente():
    print("\n=== Atualizar Cliente ===")

    id_cliente = int(input("ID do cliente a atualizar: "))

    nome = input("Novo nome: ")
    email = input("Novo email: ")
    telefone = input("Novo telefone: ")
    nif = input("Novo NIF: ")
    morada = input("Nova morada: ")

    cliente = Cliente(
        nome=nome,
        email=email,
        telefone=telefone,
        nif=nif,
        morada=morada,
        id_cliente=id_cliente
    )

    atualizar(cliente)

    print("\nCliente atualizado com sucesso!")


def eliminar_cliente():
    print("\n=== Eliminar Cliente ===")

    id_cliente = int(input("ID do cliente a eliminar: "))

    eliminar(id_cliente)

    print("\nCliente eliminado com sucesso!")


def main():
    while True:
        print("\n=== TechService ===")
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Eliminar cliente")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            atualizar_cliente()

        elif opcao == "4":
            eliminar_cliente()

        elif opcao == "0":
            print("Programa terminado.")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()