from src.database.conexao import conectar

def adicionar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO equipamento
    (id_cliente, tipo, marca, modelo, numero_serie, data_compra, observacoes)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

    valores = (
        equipamento.get_id_cliente(),
        equipamento.get_tipo(),
        equipamento.get_marca(),
        equipamento.get_modelo(),
        equipamento.get_numero_serie(),
        equipamento.get_data_compra(),
        equipamento.get_observacoes()
    )

    cursor.execute(sql, valores)
    conexao.commit()

    equipamento.id_equipamento = cursor.lastrowid

    cursor.close()
    conexao.close()

    return equipamento

def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM equipamento
        ORDER BY id_equipamento
    """

    cursor.execute(sql)
    equipamentos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return equipamentos

def atualizar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamento
        SET id_cliente = %s,
            tipo = %s,
            marca = %s,
            modelo = %s,
            numero_serie = %s,
            data_compra = %s,
            observacoes = %s
        WHERE id_equipamento = %s
    """

    valores = (
        equipamento.get_id_cliente(),
        equipamento.get_tipo(),
        equipamento.get_marca(),
        equipamento.get_modelo(),
        equipamento.get_numero_serie(),
        equipamento.get_data_compra(),
        equipamento.get_observacoes(),
        equipamento.get_id_equipamento()
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()