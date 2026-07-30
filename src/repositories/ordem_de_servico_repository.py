from src.database.conexao import conectar


def adicionar(ordem):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO ordem_de_servico
        (id_equipamento, data_abertura, defeito_relatado,
         diagnostico, solucao, status, prioridade,
         valor_servico, valor_pecas, desconto,
         valor_total, observacoes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        ordem.get_id_equipamento(),
        ordem.get_data_abertura(),
        ordem.get_defeito_relatado(),
        ordem.get_diagnostico(),
        ordem.get_solucao(),
        ordem.get_status(),
        ordem.get_prioridade(),
        ordem.get_valor_servico(),
        ordem.get_valor_pecas(),
        ordem.get_desconto(),
        ordem.get_valor_total(),
        ordem.get_observacoes()
    )

    cursor.execute(sql, valores)
    conexao.commit()

    ordem.set_id_ordem(cursor.lastrowid)

    cursor.close()
    conexao.close()

    return ordem

def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM ordem_de_servico
        ORDER BY id_ordem
    """

    cursor.execute(sql)

    ordens = cursor.fetchall()

    cursor.close()
    conexao.close()

    return ordens

def atualizar(ordem):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE ordem_de_servico
        SET id_equipamento = %s,
            defeito_relatado = %s,
            diagnostico = %s,
            solucao = %s,
            status = %s,
            prioridade = %s,
            valor_servico = %s,
            valor_pecas = %s,
            desconto = %s,
            valor_total = %s,
            observacoes = %s
        WHERE id_ordem = %s
    """

    valores = (
        ordem.get_id_equipamento(),
        ordem.get_defeito_relatado(),
        ordem.get_diagnostico(),
        ordem.get_solucao(),
        ordem.get_status(),
        ordem.get_prioridade(),
        ordem.get_valor_servico(),
        ordem.get_valor_pecas(),
        ordem.get_desconto(),
        ordem.get_valor_total(),
        ordem.get_observacoes(),
        ordem.get_id_ordem()
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()