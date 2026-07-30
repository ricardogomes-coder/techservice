-- Tabela clientes
INSERT INTO clientes (nome, email, telefone, nif, morada)
VALUES
('João Silva', 'joao.silva@email.com', '912345678', '123456789', 'Rua das Flores, Lisboa'),
('Maria Santos', 'maria.santos@email.com', '934567890', '987654321', 'Av. da Liberdade, Porto');

-- Tabela equipamento
INSERT INTO equipamento (id_cliente, tipo, marca, modelo, numero_serie, data_compra, observacoes)
VALUES
(1, 'Portátil', 'HP', 'Pavilion 15', 'HP123456789', '2023-05-10', 'Bateria com pouca autonomia'),
(2, 'Impressora', 'Epson', 'L3250', 'EP987654321', '2022-11-20', 'Não imprime a cores');

-- Tabela ordem_de_servico
INSERT INTO ordem_de_servico
(id_equipamento, data_abertura, defeito_relado, diagnostico, solucao, status, prioridade, valor_servico, valor_pecas, desconto, valor_total, observacoes)
VALUES
(1, '2026-07-30 09:00:00', 'Não liga', 'Fonte de alimentação avariada', 'Substituição da fonte', 'EM_ANDAMENTO', 'ALTA', 80.00, 40.00, 0.00, 120.00, 'A aguardar peça'),
(2, '2026-07-30 10:30:00', 'Falha na impressão', 'Cabeça de impressão entupida', 'Limpeza da cabeça de impressão', 'CONCLUIDA', 'MEDIA', 35.00, 0.00, 5.00, 30.00, 'Equipamento entregue ao cliente');

-- Tabela historico_ordem_servico
INSERT INTO historico_ordem_servico
(id_ordem, status_anterior, status_novo, observacao, data_alteracao)
VALUES
(1, 'ABERTA', 'EM_ANDAMENTO', 'Equipamento em diagnóstico', '2026-07-30 09:30:00'),
(2, 'EM_ANDAMENTO', 'CONCLUIDA', 'Reparação concluída e testada', '2026-07-30 11:30:00');