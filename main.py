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
    atualizar as atualizar_ordem,
    eliminar as eliminar_ordem
)

import flet as ft
# ---------------- CLIENTES ----------------

def menu_clientes(page: ft.Page):

    id_cliente = ft.TextField(label="ID")
    nome = ft.TextField(label="Nome")
    email = ft.TextField(label="Email")
    telefone = ft.TextField(label="Telefone")
    nif = ft.TextField(label="NIF")
    morada = ft.TextField(label="Morada")

    tabela = ft.Column()

    def carregar():

        tabela.controls.clear()

        clientes = listar_clientes()

        for c in clientes:
            tabela.controls.append(
                ft.Text(
                    f"{c['id_cliente']} | "
                    f"{c['nome']} | "
                    f"{c['email']} | "
                    f"{c['telefone']}"
                )
            )

        page.update()

    def inserir(e):

        cliente = Cliente(
            nome.value,
            email.value,
            telefone.value,
            nif.value,
            morada.value
        )

        adicionar_cliente(cliente)

        carregar()

    def atualizar(e):

        cliente = Cliente(
            nome.value,
            email.value,
            telefone.value,
            nif.value,
            morada.value,
            int(id_cliente.value)
        )

        atualizar_cliente(cliente)

        carregar()

    def eliminar(e):

        eliminar_cliente(int(id_cliente.value))

        carregar()

    page.controls.clear()

    page.add(

        ft.Text("CLIENTES", size=25),

        id_cliente,
        nome,
        email,
        telefone,
        nif,
        morada,

        ft.Row(
            [
                ft.ElevatedButton("Inserir", on_click=inserir),
                ft.ElevatedButton("Atualizar", on_click=atualizar),
                ft.ElevatedButton("Eliminar", on_click=eliminar),
                ft.ElevatedButton("Listar", on_click=lambda e: carregar()),
            ]
        ),

        tabela,

        ft.ElevatedButton(
        "Voltar",
        on_click=lambda e: menu_principal(page)
        )
    )

    carregar()

# ---------------- EQUIPAMENTOS ----------------

def menu_equipamentos(page: ft.Page):

    id_equipamento = ft.TextField(label="ID Equipamento")
    id_cliente = ft.TextField(label="ID Cliente")
    tipo = ft.TextField(label="Tipo")
    marca = ft.TextField(label="Marca")
    modelo = ft.TextField(label="Modelo")
    numero_serie = ft.TextField(label="Número de Série")
    data_compra = ft.TextField(label="Data Compra (AAAA-MM-DD)")
    observacoes = ft.TextField(label="Observações")

    tabela = ft.Column()

    def carregar():

        tabela.controls.clear()

        equipamentos = listar_equipamentos()

        for e in equipamentos:

            tabela.controls.append(
                ft.Text(
                    f"{e['id_equipamento']} | "
                    f"Cliente: {e['id_cliente']} | "
                    f"{e['tipo']} | "
                    f"{e['marca']} | "
                    f"{e['modelo']}"
                )
            )

        page.update()

    def inserir(e):

        equipamento = Equipamento(
            int(id_cliente.value),
            tipo.value,
            marca.value,
            modelo.value,
            numero_serie.value,
            data_compra.value,
            observacoes.value
        )

        adicionar_equipamento(equipamento)

        carregar()

    def atualizar(e):

        equipamento = Equipamento(
            int(id_cliente.value),
            tipo.value,
            marca.value,
            modelo.value,
            numero_serie.value,
            data_compra.value,
            observacoes.value,
            int(id_equipamento.value)
        )

        atualizar_equipamento(equipamento)

        carregar()

    def eliminar(e):

        eliminar_equipamento(int(id_equipamento.value))

        carregar()

    page.controls.clear()

    page.add(

        ft.Text("EQUIPAMENTOS", size=25),

        id_equipamento,
        id_cliente,
        tipo,
        marca,
        modelo,
        numero_serie,
        data_compra,
        observacoes,

        ft.Row(
            [
                ft.ElevatedButton("Inserir", on_click=inserir),
                ft.ElevatedButton("Atualizar", on_click=atualizar),
                ft.ElevatedButton("Eliminar", on_click=eliminar),
                ft.ElevatedButton("Listar", on_click=lambda e: carregar()),
            ]
        ),

        tabela,
        ft.ElevatedButton(
        "Voltar",
         on_click=lambda e: menu_principal(page)
        )
    )

    carregar()

def menu_ordens(page: ft.Page):

    id_ordem = ft.TextField(label="ID Ordem")
    id_equipamento = ft.TextField(label="ID Equipamento")
    data_abertura = ft.TextField(label="Data (AAAA-MM-DD HH:MM:SS)")
    defeito_relatado = ft.TextField(label="Defeito Relatado")
    diagnostico = ft.TextField(label="Diagnóstico")
    solucao = ft.TextField(label="Solução")
    status = ft.TextField(label="Status")
    prioridade = ft.TextField(label="Prioridade")
    valor_servico = ft.TextField(label="Valor Serviço")
    valor_pecas = ft.TextField(label="Valor Peças")
    desconto = ft.TextField(label="Desconto")
    observacoes = ft.TextField(label="Observações")

    tabela = ft.Column()

    def carregar():

        tabela.controls.clear()

        ordens = listar_ordens()

        for o in ordens:

            tabela.controls.append(
                ft.Text(
                    f"{o['id_ordem']} | "
                    f"{o['nome']} | "
                    f"{o['marca']} | "
                    f"{o['modelo']} | "
                    f"{o['data_abertura']} | "
                    f"{o['status']} | "
                    f"{o['prioridade']} | "
                    f"{o['valor_total']} €"
                )
            )

        page.update()

    def inserir(e):

        total = (
            float(valor_servico.value)
            + float(valor_pecas.value)
            - float(desconto.value)
        )

        ordem = OrdemServico(
            int(id_equipamento.value),
            data_abertura.value,
            defeito_relatado.value,
            diagnostico.value,
            solucao.value,
            status.value,
            prioridade.value,
            float(valor_servico.value),
            float(valor_pecas.value),
            float(desconto.value),
            total,
            observacoes.value
        )

        adicionar_ordem(ordem)

        carregar()

    def atualizar(e):

        total = (
            float(valor_servico.value)
            + float(valor_pecas.value)
            - float(desconto.value)
        )

        ordem = OrdemServico(
            int(id_equipamento.value),
            None,
            defeito_relatado.value,
            diagnostico.value,
            solucao.value,
            status.value,
            prioridade.value,
            float(valor_servico.value),
            float(valor_pecas.value),
            float(desconto.value),
            total,
            observacoes.value,
            int(id_ordem.value)
        )

        atualizar_ordem(ordem)

        carregar()

    def eliminar(e):

        eliminar_ordem(int(id_ordem.value))

        carregar()

    page.controls.clear()

    page.add(

        ft.Text(
            "ORDENS DE SERVIÇO",
            size=25
        ),

        id_ordem,
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
        observacoes,

        ft.Row(
            [
                ft.ElevatedButton("Abrir Ordem", on_click=inserir),
                ft.ElevatedButton("Atualizar", on_click=atualizar),
                ft.ElevatedButton("Eliminar", on_click=eliminar),
                ft.ElevatedButton("Listar", on_click=lambda e: carregar()),
            ]
        ),

        tabela,

        ft.ElevatedButton(
        "Voltar",
        on_click=lambda e: menu_principal(page)
)
    )

    carregar()
# ---------------- MENU PRINCIPAL ----------------
def menu_principal(page: ft.Page):

    page.controls.clear()

    page.add(
        ft.Text(
            "TECHSERVICE",
            size=30,
            weight=ft.FontWeight.BOLD
        ),

        ft.ElevatedButton(
            "Clientes",
            on_click=lambda e: menu_clientes(page)
        ),

        ft.ElevatedButton(
            "Equipamentos",
            on_click=lambda e: menu_equipamentos(page)
        ),

        ft.ElevatedButton(
            "Ordens de Serviço",
            on_click=lambda e: menu_ordens(page)
        )
    )

    page.update()

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.title = "TECHSERVICE"
    page.window.width = 900
    page.window.height = 700

    menu_principal(page)

ft.app(target=main)


if __name__ == "__main__":
    main()