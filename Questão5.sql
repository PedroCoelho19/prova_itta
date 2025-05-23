CREATE TABLE pedidos (
  id INT PRIMARY KEY,
  cliente_id INT,
  valor_total DECIMAL(10, 2),
  data_pedido DATE
 );
 CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nome VARCHAR(100)
 );

-- Escreva uma consulta SQL que retorne o nome dos clientes e o valor total somado de seus
--  pedidos, ordenados do maior para o menor valor.


select nome,valor_total from clientes,pedidos ORDER BY valor_total DESC;