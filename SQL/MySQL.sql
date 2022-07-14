-- criar banco de dados

create database nome_do_banco_de_dados;


-- Criar uma tabela no banco de dados

CREATE TABLE nome_da_tabela(
    coluna1 INT PRIMARY KEY AUTOINCREMENT,
    coluna2 VARCHAR(tamanho),
    coluna3 DATE
);

-- Inserir

INSERT INTO tabela(coluna1, coluna2, coluna3) VALUES('valor1', 'valor2', 'valor3');

--Selecionando algum valor

SELECT * FROM tabela -- retorna todos os itens da tabela

SELECT nome_da_coluna FROM tabela retorna tudo que tiver naquela coluna1

-- Alterando um valor

UPDATE tabela SET informação = 'novainformação' WHERE item=item