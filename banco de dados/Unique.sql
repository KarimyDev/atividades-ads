use aula;
create table cidade (
id int primary key,
nome varchar(100),
sigla char(03) unique);

insert into cidade (id, nome, sigla) values (1, 'Curitiba', 'CWB');
select * from cidade;

insert into cidade (id, nome, sigla) values (2, 'Natal', 'NTA');
select * from cidade;

create table cliente (
id int primary key,
nome varchar(100),
idcidade int,
constraint fkclienteCidade foreign key (idcidade) references cidade(id) );

insert into cliente values(1,'Joao', 1);
insert into cliente values(2,'Jose', 10);
describe aluno;