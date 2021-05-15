--
-- Cria view para poder realizar contagem das operacoes
--
CREATE VIEW count_operacao AS select cp.cesta_id,op.nome from compra cp join operacao op on cp.operacao_id = op."id" GROUP BY cp.cesta_id,op.nome

--
-- Cria view para poder fazer a conta do ticket médio
--
CREATE VIEW   count_cesta AS select cs."id",cs.valor,o.nome 
	from compra cp 
		join operacao o on o."id" = cp.operacao_id 
		join cesta cs on cs."id" = cp.cesta_id
group by cs."id",cs.valor,o.nome


--
-- View para realizar as contagens das datas
--
create view count_data as select cs."id",d.mes, d.dia_da_semana, dia_util, cp.loja_id
	from compra cp 
		join cesta cs on cs."id" = cp.cesta_id
		join data d on d.id = cp.data_id
group by cs."id",d.mes, d.dia_da_semana, dia_util, cp.loja_id

--
-- Query  vendas por mes
--

SELECT d.mes, "count"(*) as qtd
	From compra cp 
		JOIN "data" d on d."id" = cp.data_id 
group by d.mes ORDER BY qtd desc;

--
-- Vendas por mês loja
-- 
SELECT d.mes, "count"(*) as qtd
	From compra cp 
		JOIN "data" d on d."id" = cp.data_id WHERE cp.loja_id = 2
group by d.mes ORDER BY qtd desc;

--
-- Consulta para calcular o Ticket Médio
-- regex para rodar no arquivo devido a essa query [0-9]\.[0-9]*\.[0-9]*
select AVG(CAST(valor as float)) from count_cesta where nome = 	'Venda'	;

--
-- Contagem da  operacao 
--
select nome, count(*) as qtd from count_operacao group by nome order by qtd desc