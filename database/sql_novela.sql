DROP DATABASE IF EXISTS trainee;
CREATE DATABASE trainee;

USE trainee;

CREATE TABLE tbNovela
(codigo_novela INT,
nome_novela VARCHAR(30) NOT NULL,
data_primeiro_capitulo DATE,
data_ultimo_capitulo DATE,
horario_exibicao TIME,
CONSTRAINT pk_tbNovela PRIMARY KEY (codigo_novela)
);

CREATE TABLE tbAtor
(codigo_ator INT,
nome_ator VARCHAR(20) NOT NULL,
idade INT,
cidade_ator VARCHAR(20),
salario_ator FLOAT,
sexo_ator CHAR(1),
CONSTRAINT pk_tbAtor PRIMARY KEY (codigo_ator)
);

CREATE TABLE tbCapitulo
(codigo_capitulo INT,
nome_capitulo VARCHAR(50) NOT NULL,
data_exibicao_capitulo DATE,

codigo_novela INT,
CONSTRAINT pk_tbCapitulo PRIMARY KEY (codigo_capitulo),
CONSTRAINT fk_tbCapitulo_tbNovela FOREIGN KEY (codigo_novela)
REFERENCES tbNovela (codigo_novela) ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE tbPersonagem
(codigo_personagem INT,
nome_personagem VARCHAR(50) NOT NULL,
idade_personagem INT,
situacao_fnanceira_personagem VARCHAR(20),
codigo_ator INT,
CONSTRAINT pk_tbPersonagem PRIMARY KEY (codigo_personagem),
CONSTRAINT fk_tbPersonagem_tbAtor FOREIGN KEY (codigo_ator)
REFERENCES tbAtor (codigo_ator) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE tbNovelaPersonagem
(codigo_personagem INT,
codigo_novela INT,
CONSTRAINT pk_tbNovelaPersonagem PRIMARY KEY (codigo_personagem,codigo_novela),
CONSTRAINT fk_tbNovelaPersonagem_tbPersonagem FOREIGN KEY (codigo_personagem)
REFERENCES tbPersonagem (codigo_personagem) ON DELETE CASCADE
ON UPDATE CASCADE,
CONSTRAINT fk_tbNovelaPersonagem_tbNovela FOREIGN KEY (codigo_novela)
REFERENCES tbNovela (codigo_novela) ON DELETE CASCADE
ON UPDATE CASCADE
);

SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM tbNovela;
-- DELETE FROM tbAtor;
DELETE FROM tbCapitulo;
-- DELETE FROM tbPersonagem;
-- DELETE FROM tbNovelaPersonagem;