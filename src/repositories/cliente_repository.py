from src.database.conexao import conectar


def adicionar(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO clientes (nome, email, telefone, nif, morada)
        VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        cliente.get_nome(),
        cliente.get_email(),
        cliente.get_telefone(),
        cliente.get_nif(),
        cliente.get_morada()
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cliente.id_cliente = cursor.lastrowid

    cursor.close()
    conexao.close()

    return cliente

def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_cliente, nome, email, telefone, nif, morada,
               status, data_cadatro, data_alteracao, data_eliminacao
        FROM clientes
        WHERE status = 1
        ORDER BY id_cliente
    """

    cursor.execute(sql)
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()
    return clientes

def atualizar(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE clientes
        SET nome = %s,
            email = %s,
            telefone = %s,
            data_alteracao = NOW()
        WHERE id_cliente = %s
          AND status = 1
    """
    valores = (cliente.nome, cliente.email, cliente.telefone, cliente.id_cliente)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def excluir(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE clientes
        SET status = 0,
            data_eliminacao = NOW()
        WHERE id_cliente = %s
          AND status = 1
    """

    cursor.execute(sql, (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()
