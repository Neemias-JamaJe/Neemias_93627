CREATE DATABASE loja_nemo;
USE loja_nemo;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL
);


CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50),
    senha VARCHAR(50)
);
describe usuarios;
select * from usuarios;
select * from produtos;