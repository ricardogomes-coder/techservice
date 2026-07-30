from src.models.cliente import Cliente
from src.models.equipamento import Equipamento
from src.repositories.cliente_repository import (
    adicionar as adicionar_cliente,
    listar as listar_clientes,
    atualizar as atualizar_cliente,
    eliminar as eliminar_cliente
)

from src.repositories.equipamento_repository import (
    adicionar as adicionar_equipamento,
    listar as listar_equipamentos,
    atualizar as atualizar_equipamento,
    eliminar as eliminar_equipamento
)
from src.models.ordem_de_servico import OrdemServico

from src.repositories.ordem_de_servico_repository import (
    adicionar as adicionar_ordem,
    listar as listar_ordens,
    atualizar as atualizar_ordem
)

# ---------------- CLIENTES ----------------

def menu_clientes():

    while True:
        print("\n=== CLIENTES ===")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Eliminar")
        print("0 - Voltar")

        opcao = input("Opção: ")

        if opcao == "1":

            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            nif = input("NIF: ")
            morada = input("Morada: ")

            cliente = Cliente(nome, email, telefone, nif, morada)

            adicionar_cliente(cliente)

            print("\nCliente inserido com sucesso!")

        elif opcao == "2":

            clientes = listar_clientes()

            for c in clientes:
                print("-----------------------")
                print(f"ID: {c['id_cliente']}")
                print(f"Nome: {c['nome']}")
                print(f"Email: {c['email']}")
                print(f"Telefone: {c['telefone']}")

        elif opcao == "3":

            id_cliente = int(input("ID: "))
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            nif = input("NIF: ")
            morada = input("Morada: ")

            cliente = Cliente(nome, email, telefone, nif, morada, id_cliente)

            atualizar_cliente(cliente)

            print("Cliente atualizado!")

        elif opcao == "4":

            id_cliente = int(input("ID: "))

            eliminar_cliente(id_cliente)

            print("Cliente eliminado!")

        elif opcao == "0":
            break


# ---------------- EQUIPAMENTOS ----------------

def menu_equipamentos():

    while True:
        print("\n=== EQUIPAMENTOS ===")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Eliminar")
        print("0 - Voltar")

        opcao = input("Opção: ")

        if opcao == "1":

            id_cliente = int(input("ID do Cliente: "))
            tipo = input("Tipo: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            numero_serie = input("Número de Série: ")
            data_compra = input("Data Compra (AAAA-MM-DD): ")
            observacoes = input("Observações: ")

            equipamento = Equipamento(
                id_cliente,
                tipo,
                marca,
                modelo,
                numero_serie,
                data_compra,
                observacoes
            )

            adicionar_equipamento(equipamento)

            print("\nEquipamento inserido!")

        elif opcao == "2":

            equipamentos = listar_equipamentos()

            for e in equipamentos:
                print("-----------------------")
                print(f"ID: {e['id_equipamento']}")
                print(f"Cliente: {e['id_cliente']}")
                print(f"Tipo: {e['tipo']}")
                print(f"Marca: {e['marca']}")
                print(f"Modelo: {e['modelo']}")

        elif opcao == "3":

            id_equipamento = int(input("ID do Equipamento: "))
            id_cliente = int(input("ID do Cliente: "))
            tipo = input("Tipo: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            numero_serie = input("Número de Série: ")
            data_compra = input("Data Compra: ")
            observacoes = input("Observações: ")

            equipamento = Equipamento(
                id_cliente,
                tipo,
                marca,
                modelo,
                numero_serie,
                data_compra,
                observacoes,
                id_equipamento
            )

            atualizar_equipamento(equipamento)

            print("Equipamento atualizado!")

        elif opcao == "4":

            id_equipamento = int(input("ID do Equipamento: "))

            eliminar_equipamento(id_equipamento)

            print("Equipamento eliminado!")

        elif opcao == "0":
            break

def menu_ordens():

    while True:

        print("\n=== ORDENS DE SERVIÇO ===")
        print("1 - Abrir Ordem")
        print("2 - Listar Ordens")
        print("3 - Atualizar Ordem")
        print("0 - Voltar")

        opcao = input("Opção: ")

        if opcao == "1":

            id_equipamento = int(input("ID do Equipamento: "))
            data_abertura = input("Data de abertura (AAAA-MM-DD HH:MM:SS): ")
            defeito_relatado = input("Defeito relatado: ")
            diagnostico = input("Diagnóstico: ")
            solucao = input("Solução: ")
            status = input("Status: ")
            prioridade = input("Prioridade: ")

            valor_servico = float(input("Valor do serviço: "))
            valor_pecas = float(input("Valor das peças: "))
            desconto = float(input("Desconto: "))

            valor_total = valor_servico + valor_pecas - desconto

            observacoes = input("Observações: ")

            ordem = OrdemServico(
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
                observacoes
            )

            adicionar_ordem(ordem)

            print("\nOrdem de Serviço aberta com sucesso!")

        elif opcao == "2":

            ordens = listar_ordens()

            for o in ordens:

                print("----------------------------")
                print(f"ID: {o['id_ordem']}")
                print(f"Cliente: {o['nome']}")
                print(f"Marca: {o['marca']}")
                print(f"Modelo: {o['modelo']}")
                print(f"Data: {o['data_abertura']}")
                print(f"Estado: {o['status']}")
                print(f"Prioridade: {o['prioridade']}")
                print(f"Valor Total: {o['valor_total']}")

        elif opcao == "3":

            id_ordem = int(input("ID da Ordem: "))
            id_equipamento = int(input("ID do Equipamento: "))
            defeito_relatado = input("Defeito relatado: ")
            diagnostico = input("Diagnóstico: ")
            solucao = input("Solução: ")
            status = input("Status: ")
            prioridade = input("Prioridade: ")

            valor_servico = float(input("Valor do serviço: "))
            valor_pecas = float(input("Valor das peças: "))
            desconto = float(input("Desconto: "))

            valor_total = valor_servico + valor_pecas - desconto

            observacoes = input("Observações: ")

            ordem = OrdemServico(
                id_equipamento,
                None,
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
                id_ordem
            )

            atualizar_ordem(ordem)

            print("\nOrdem atualizada com sucesso!")

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

# ---------------- MENU PRINCIPAL ----------------

def main():

    while True:

        print("\n========== TECHSERVICE ==========")
        print("1 - Clientes")
        print("2 - Equipamentos")
        print("3 - Ordens de Serviço")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()

        elif opcao == "2":
            menu_equipamentos()

        elif opcao == "3":
            menu_ordens()
            
        elif opcao == "0":
            print("Programa terminado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()