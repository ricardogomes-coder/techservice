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

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Telefone")),
        ],
        rows=[]
    )

    def mensagem(texto):
        page.snack_bar = ft.SnackBar(ft.Text(texto))
        page.snack_bar.open = True
        page.update()

    def limpar():
        id_cliente.value = ""
        nome.value = ""
        email.value = ""
        telefone.value = ""
        nif.value = ""
        morada.value = ""

    def carregar():
        tabela.rows.clear()
        clientes = listar_clientes()

        for c in clientes:

            tabela.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(c["id_cliente"]))),
                        ft.DataCell(ft.Text(c["nome"])),
                        ft.DataCell(ft.Text(c["email"])),
                        ft.DataCell(ft.Text(c["telefone"])),
                    ]
                )
            )

        page.update()

    def inserir(e):

        if nome.value == "" or email.value == "":
            mensagem("Preencha Nome e Email.")
            return

        cliente = Cliente(
            nome.value,
            email.value,
            telefone.value,
            nif.value,
            morada.value
        )

        adicionar_cliente(cliente)

        limpar()
        carregar()

        mensagem("Cliente inserido com sucesso!")

    def atualizar(e):

        if id_cliente.value == "":
            mensagem("Introduza o ID.")
            return

        try:
            id = int(id_cliente.value)
        except ValueError:
            mensagem("ID inválido.")
            return

        cliente = Cliente(
            nome.value,
            email.value,
            telefone.value,
            nif.value,
            morada.value,
            id
        )

        atualizar_cliente(cliente)

        limpar()
        carregar()

        mensagem("Cliente atualizado!")

    def eliminar(e):

        if id_cliente.value == "":
            mensagem("Introduza o ID.")
            return

        try:
            id = int(id_cliente.value)
        except ValueError:
            mensagem("ID inválido.")
            return

        eliminar_cliente(id)

        limpar()
        carregar()

        mensagem("Cliente eliminado!")

    page.controls.clear()

    page.add(

        ft.Text(
            "CLIENTES",
            size=25,
            weight=ft.FontWeight.BOLD
        ),

        id_cliente,
        nome,
        email,
        telefone,
        nif,
        morada,

        ft.Row(
            [
                ft.ElevatedButton(
                    "Inserir",
                    on_click=inserir
                ),

                ft.ElevatedButton(
                    "Atualizar",
                    on_click=atualizar
                ),

                ft.ElevatedButton(
                    "Eliminar",
                    on_click=eliminar
                ),

                ft.ElevatedButton(
                    "Atualizar Lista",
                    on_click=lambda e: carregar()
                ),
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
    observacoes = ft.TextField(
        label="Observações",
        multiline=True
    )

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Cliente")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Marca")),
            ft.DataColumn(ft.Text("Modelo")),
        ],
        rows=[]
    )

    def mensagem(texto):

        page.snack_bar = ft.SnackBar(
            ft.Text(texto)
        )

        page.snack_bar.open = True
        page.update()


    def limpar():

        id_equipamento.value = ""
        id_cliente.value = ""
        tipo.value = ""
        marca.value = ""
        modelo.value = ""
        numero_serie.value = ""
        data_compra.value = ""
        observacoes.value = ""

        page.update()


    def carregar():
        tabela.rows.clear()
        equipamentos = listar_equipamentos()

        for e in equipamentos:
            tabela.rows.append(
                ft.DataRow(
                    cells=[

                        ft.DataCell(
                            ft.Text(
                                str(e["id_equipamento"])
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(e["id_cliente"])
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                e["tipo"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                e["marca"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                e["modelo"]
                            )
                        ),
                    ]
                )
            )

        page.update()

    def inserir(e):

        if id_cliente.value == "" or tipo.value == "":
            mensagem(
                "ID Cliente e Tipo são obrigatórios."
            )
            return

        try:
            id_cli = int(id_cliente.value)
        except ValueError:

            mensagem(
                "ID Cliente inválido."
            )
            return

        equipamento = Equipamento(

            id_cli,
            tipo.value,
            marca.value,
            modelo.value,
            numero_serie.value,
            data_compra.value,
            observacoes.value
        )
        adicionar_equipamento(equipamento)

        limpar()
        carregar()

        mensagem(
            "Equipamento inserido com sucesso!"
        )


    def atualizar(e):
        if id_equipamento.value == "":
            mensagem(
                "Introduza o ID do equipamento."
            )
            return


        try:
            id_eq = int(id_equipamento.value)
            id_cli = int(id_cliente.value)

        except ValueError:

            mensagem(
                "IDs inválidos."
            )
            return

        equipamento = Equipamento(

            id_cli,
            tipo.value,
            marca.value,
            modelo.value,
            numero_serie.value,
            data_compra.value,
            observacoes.value,
            id_eq
        )

        atualizar_equipamento(equipamento)
        limpar()
        carregar()

        mensagem(
            "Equipamento atualizado!"
        )


    def eliminar(e):

        if id_equipamento.value == "":
            mensagem(
                "Introduza o ID do equipamento."
            )
            return

        try:
            id_eq = int(id_equipamento.value)
        except ValueError:
            mensagem(
                "ID inválido."
            )
            return

        eliminar_equipamento(id_eq)

        limpar()
        carregar()

        mensagem(
            "Equipamento eliminado!"
        )

    page.controls.clear()

    page.add(

        ft.Text(
            "EQUIPAMENTOS",
            size=25,
            weight=ft.FontWeight.BOLD
        ),

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
                ft.ElevatedButton(
                    "Inserir",
                    on_click=inserir
                ),

                ft.ElevatedButton(
                    "Atualizar",
                    on_click=atualizar
                ),

                ft.ElevatedButton(
                    "Eliminar",
                    on_click=eliminar
                ),

                ft.ElevatedButton(
                    "Atualizar Lista",
                    on_click=lambda e: carregar()
                ),

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

    data_abertura = ft.TextField(
        label="Data Abertura (AAAA-MM-DD HH:MM:SS)"
    )

    defeito_relatado = ft.TextField(
        label="Defeito Relatado",
        multiline=True
    )

    diagnostico = ft.TextField(
        label="Diagnóstico",
        multiline=True
    )

    solucao = ft.TextField(
        label="Solução",
        multiline=True
    )
    status = ft.Dropdown(
        label="Status",
        options=[
            ft.dropdown.Option("ABERTA"),
            ft.dropdown.Option("EM_ANDAMENTO"),
            ft.dropdown.Option("AGUARDANDO_PECAS"),
            ft.dropdown.Option("CONCLUIDA"),
        ]
    )
    prioridade = ft.Dropdown(
        label="Prioridade",
        options=[
            ft.dropdown.Option("BAIXA"),
            ft.dropdown.Option("MEDIA"),
            ft.dropdown.Option("ALTA"),
        ]
    )

    valor_servico = ft.TextField(
        label="Valor Serviço"
    )

    valor_pecas = ft.TextField(
        label="Valor Peças"
    )

    desconto = ft.TextField(
        label="Desconto"
    )

    valor_total = ft.TextField(
        label="Valor Total",
        read_only=True
    )

    observacoes = ft.TextField(
        label="Observações",
        multiline=True
    )

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Cliente")),
            ft.DataColumn(ft.Text("Marca")),
            ft.DataColumn(ft.Text("Modelo")),
            ft.DataColumn(ft.Text("Estado")),
            ft.DataColumn(ft.Text("Prioridade")),
            ft.DataColumn(ft.Text("Total")),
        ],

        rows=[]
    )

    def mensagem(texto):

        page.snack_bar = ft.SnackBar(
            ft.Text(texto)
        )

        page.snack_bar.open = True
        page.update()

    def calcular_total(e=None):
        try:
            servico = float(
                valor_servico.value or 0
            )

            pecas = float(
                valor_pecas.value or 0
            )

            desc = float(
                desconto.value or 0
            )

            total = servico + pecas - desc

            valor_total.value = str(total)

            page.update()

        except ValueError:

            valor_total.value = "0"



    def limpar():

        id_ordem.value = ""
        id_equipamento.value = ""
        data_abertura.value = ""
        defeito_relatado.value = ""
        diagnostico.value = ""
        solucao.value = ""
        status.value = None
        prioridade.value = None
        valor_servico.value = ""
        valor_pecas.value = ""
        desconto.value = ""
        valor_total.value = ""
        observacoes.value = ""
        page.update()



    def carregar():
        tabela.rows.clear()
        ordens = listar_ordens()

        for o in ordens:


            tabela.rows.append(

                ft.DataRow(

                    cells=[

                        ft.DataCell(
                            ft.Text(
                                str(o["id_ordem"])
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                o["nome"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                o["marca"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                o["modelo"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                o["status"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                o["prioridade"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(o["valor_total"])
                            )
                        ),

                    ]

                )

            )
        page.update()

    def inserir(e):
        if (
            id_equipamento.value == ""
            or status.value is None
            or prioridade.value is None
        ):

            mensagem(
                "Preencha equipamento, status e prioridade."
            )

            return

        try:

            equipamento = int(
                id_equipamento.value
            )

            total = float(
                valor_total.value or 0
            )


        except ValueError:

            mensagem(
                "Valores inválidos."
            )

            return
        
        ordem = OrdemServico(

            equipamento,
            data_abertura.value,
            defeito_relatado.value,
            diagnostico.value,
            solucao.value,
            status.value,
            prioridade.value,
            float(valor_servico.value or 0),
            float(valor_pecas.value or 0),
            float(desconto.value or 0),
            total,
            observacoes.value
        )

        adicionar_ordem(ordem)

        limpar()
        carregar()

        mensagem(
            "Ordem aberta com sucesso!"
        )



    def atualizar(e):
        if id_ordem.value == "":

            mensagem(
                "Indique o ID da ordem."
            )

            return
        
        ordem = OrdemServico(

            int(id_equipamento.value),
            None,
            defeito_relatado.value,
            diagnostico.value,
            solucao.value,
            status.value,
            prioridade.value,
            float(valor_servico.value or 0),
            float(valor_pecas.value or 0),
            float(desconto.value or 0),
            float(valor_total.value or 0),
            observacoes.value,
            int(id_ordem.value)

        )

        atualizar_ordem(ordem)

        limpar()
        carregar()

        mensagem(
            "Ordem atualizada!"
        )


    def eliminar(e):

        if id_ordem.value == "":

            mensagem(
                "Indique o ID da ordem."
            )

            return

        eliminar_ordem(
            int(id_ordem.value)
        )

        limpar()
        carregar()
        mensagem(
            "Ordem eliminada!"
        )
    valor_servico.on_change = calcular_total
    valor_pecas.on_change = calcular_total
    desconto.on_change = calcular_total



    page.controls.clear()


    page.add(

        ft.Text(
            "ORDENS DE SERVIÇO",
            size=25,
            weight=ft.FontWeight.BOLD
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
        valor_total,
        observacoes,


        ft.Row(
            [
                ft.ElevatedButton(
                    "Abrir Ordem",
                    on_click=inserir
                ),

                ft.ElevatedButton(
                    "Atualizar",
                    on_click=atualizar
                ),

                ft.ElevatedButton(
                    "Eliminar",
                    on_click=eliminar
                ),

                ft.ElevatedButton(
                    "Atualizar Lista",
                    on_click=lambda e: carregar()
                ),

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