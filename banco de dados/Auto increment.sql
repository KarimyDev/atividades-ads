create table cidade (
id int primary key auto_increment,
nome varchar(120) not null,
cepgeral int unsigned zerofill);

alter table cidade
-- add, modify, change drop
add dddd char(05);
describe cidade

alter table cidade
change dddd ddd chat(05);

alter table cidade
modify ddd char(03);

insert into cidade (nome, cepgeral, ddd)
values('Salvador', 76599, 045);

insert into cidade (nome, cepgeral, ddd)
values('Rio de Janeiro', 98599, 021);

select * from cidade;