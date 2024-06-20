create database crm_db;

USE crm_db;

create table clientes (

id int auto_increment primary key,
nome varchar (50) not null,
sobre_nome varchar (50) not null,
telefone varchar (20) not null,
email varchar (30) not null

);
insert into clientes (nome, sobre_nome, telefone, email) 
values ( 'Rafael', 'Costa','991323468', 'rafael@gmail.com'); 

create table historico (

chamadas_telefonicas int auto_increment primary key,
cliente_id int,
dia_chamada varchar (30),
tipo_de_contato varchar (50),
notas varchar (100),
foreign key (cliente_id) references clientes(id)
);
insert into historico ( cliente_id, dia_chamada, tipo_de_contato, notas)
values (1, '03/05/2004', 'comercial', 'cliente mostra interesse no produto');

create table oportunidade_vendas (

id int auto_increment primary key,
cliente_id int,
descricao_oportunidade varchar (100),
valor_estimado varchar(30),
tipo_venda varchar (50),
notas varchar (100),
foreign key (cliente_id) references clientes(id)
);

insert into oportunidade_vendas ( cliente_id, descricao_oportunidade, valor_estimado, tipo_venda, notas)
values (1,'venda direta', '2.000', 'a vista', 'o cliente pretende comprar o produto');


 














