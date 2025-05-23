 
 CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  cidade VARCHAR(100),
  idade INT
 );


SELECT nome,cidade FROM clientes WHERE cidade = "São Paulo"

