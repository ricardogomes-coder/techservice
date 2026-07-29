DROP DATABASE IF EXISTS techservice_db;

CREATE DATABASE techservice_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE techservice_db;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telefone VARCHAR(20),
    nif VARCHAR(20) UNIQUE,
    morada VARCHAR(200),
    status TINYINT NOT NULL DEFAULT 1,
    data_cadatro DATETIME not null default current_timestamp,
    data_alteracao DATETIME,
    data_eliminacao DATETIME
) ENGINE=InnoDB;

CREATE TABLE equipamento (
	id_equipamento INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente int not null,
    tipo VARCHAR(50),
    marca VARCHAR(50),
    modelo VARCHAR(50),
    numero_serie VARCHAR(100) UNIQUE,
    data_compra date,
    observacoes VARCHAR(200),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)ENGINE=InnoDB;

CREATE TABLE ordem_de_servico (
    id_ordem INT AUTO_INCREMENT PRIMARY KEY,
    id_equipamento INT NOT NULL,
    data_abertura DATETIME NOT NULL,
    defeito_relado VARCHAR(500),
    diagnostico VARCHAR(500),
    solucao VARCHAR(500),
	status ENUM('ABERTA', 'EM_ANDAMENTO', 'AGUARDANDO_PECAS', 'CONCLUIDA') NOT NULL DEFAULT 'ABERTA',
	prioridade ENUM('BAIXA', 'MEDIA', 'ALTA') NOT NULL DEFAULT 'MEDIA',
	valor_servico DECIMAL(10,2) DEFAULT 0.00,
    valor_pecas DECIMAL(10,2) DEFAULT 0.00,
    desconto DECIMAL(10,2) DEFAULT 0.00,
    valor_total DECIMAL(10,2) DEFAULT 0.00,
	observacoes VARCHAR(300),
	FOREIGN KEY (id_equipamento) REFERENCES equipamento(id_equipamento)
)ENGINE=InnoDB;

CREATE TABLE historico_ordem_servico(
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem INT NOT NULL,
	status_anterior VARCHAR(50) NULL,
    status_novo VARCHAR(50) NOT NULL,
    observacao VARCHAR(300),
    data_alteracao DATETIME,
    data_eliminacao DATETIME,
	FOREIGN KEY (id_ordem) REFERENCES ordem_de_servico(id_ordem)
)ENGINE=InnoDB;