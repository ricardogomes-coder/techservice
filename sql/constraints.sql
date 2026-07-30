USE techservice_db;

ALTER TABLE equipamento
ADD CONSTRAINT fk_equip_cliente
FOREIGN KEY (id_cliente)
REFERENCES clientes(id_cliente)
ON UPDATE CASCADE
ON DELETE RESTRICT;


ALTER TABLE ordem_de_servico
ADD CONSTRAINT fk_os_equipamento
FOREIGN KEY (id_equipamento)
REFERENCES equipamento(id_equipamento)
ON UPDATE CASCADE
ON DELETE RESTRICT;