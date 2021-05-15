--CREATE DATABASE pier OWNER pier  WITH ENCODING 'UTF-8';

CREATE SEQUENCE dicionario_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE modelo_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE genero_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE tamanho_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE cor_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE loja_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE material_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE colecao_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE cesta_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE data_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE tipo_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE item_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE compra_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE faixa_etaria_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

 CREATE SEQUENCE estado_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE SEQUENCE operacao_id_seq
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;

CREATE TABLE dicionario (
 id integer NOT NULL DEFAULT nextval('dicionario_id_seq'),
 palavra varchar(100) NOT NULL UNIQUE,
 frequencia integer NOT NULL
);
ALTER TABLE dicionario ADD PRIMARY KEY (id);

CREATE TABLE modelo (
 id integer NOT NULL DEFAULT nextval('modelo_id_seq'),
 nome varchar(100) NOT NULL,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE modelo ADD PRIMARY KEY (id);

CREATE TABLE genero (
 id integer NOT NULL DEFAULT nextval('genero_id_seq'),
 nome varchar(100) NOT NULL UNIQUE,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE genero ADD PRIMARY KEY (id);

CREATE TABLE tamanho (
 id integer NOT NULL DEFAULT nextval('tamanho_id_seq'),
 nome varchar(100) NOT NULL,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE tamanho ADD PRIMARY KEY (id);


CREATE TABLE cor (
 id integer NOT NULL DEFAULT nextval('cor_id_seq'),
 nome varchar(100) NOT NULL UNIQUE,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE cor ADD PRIMARY KEY (id);


CREATE TABLE loja (
 id integer NOT NULL DEFAULT nextval('loja_id_seq'),
 nome varchar(100) NOT NULL UNIQUE,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE loja ADD PRIMARY KEY (id);


CREATE TABLE material (
 id integer NOT NULL DEFAULT nextval('material_id_seq'),
 nome varchar(100) NOT NULL UNIQUE,
 pattern varchar(100) NOT NULL UNIQUE
);

ALTER TABLE material ADD PRIMARY KEY (id);

CREATE TABLE colecao (
 id integer NOT NULL DEFAULT nextval('colecao_id_seq'),
 nome varchar(100) NOT NULL UNIQUE,
 pattern varchar(100) NOT NULL UNIQUE
);


ALTER TABLE colecao ADD PRIMARY KEY (id);


CREATE TABLE cesta (
 id integer NOT NULL DEFAULT nextval('cesta_id_seq'),
 qtd_pecas integer NOT NULL,
 valor varchar(10) NOT NULL,
 codigo integer NOT NULL,
 loja integer NOT NULL
);
ALTER TABLE cesta ADD PRIMARY KEY (id);

CREATE TABLE data (
 id integer NOT NULL DEFAULT nextval('data_id_seq'),
 data Date,
 estacao varchar(45),
 status varchar(45),
 dia_util integer,
 dia_da_semana varchar(45),
 mes varchar(45)
);
ALTER TABLE data ADD PRIMARY KEY (id);


CREATE TABLE item (
 id integer NOT NULL DEFAULT nextval('item_id_seq'),
 nome varchar(45) NOT NULL,
 tipo varchar(100) NOT NULL,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE item ADD PRIMARY KEY (id);


CREATE TABLE tipo (
 id integer NOT NULL DEFAULT nextval('tipo_id_seq'),
 nome varchar(45) NOT NULL,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE tipo ADD PRIMARY KEY (id);

CREATE TABLE estado (
 id integer NOT NULL DEFAULT nextval('estado_id_seq'),
 nome varchar(45) NOT NULL,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE estado ADD PRIMARY KEY (id);

CREATE TABLE faixa_etaria (
 id integer NOT NULL DEFAULT nextval('faixa_etaria_id_seq'),
 nome varchar(45) NOT NULL,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE faixa_etaria ADD PRIMARY KEY (id);

CREATE TABLE operacao (
 id integer NOT NULL DEFAULT nextval('operacao_id_seq'),
 nome varchar(45) NOT NULL,
 pattern varchar(100) NOT NULL UNIQUE
);
ALTER TABLE operacao ADD PRIMARY KEY (id);


CREATE TABLE compra (
  id integer NOT NULL DEFAULT nextval('compra_id_seq') PRIMARY KEY,
  cesta_id integer,
  colecao_id integer,
  cor_id integer,
  data_id integer,
  genero_id integer,
  loja_id  integer,
  material_id integer,
  modelo_id integer,
  item_id integer,
  tamanho_id integer,
  tipo_id integer,
  operacao_id integer,
  faixa_etaria_id integer,
  estado_id integer,
  valor varchar(100) NOT NULL,
  qtd integer NOT NULL,
  FOREIGN KEY (cesta_id) REFERENCES cesta (id),
  FOREIGN KEY (colecao_id) REFERENCES colecao (id),
  FOREIGN KEY (cor_id) REFERENCES cor (id),
  FOREIGN KEY (data_id) REFERENCES data (id),
  FOREIGN KEY (genero_id) REFERENCES genero (id),
  FOREIGN KEY (loja_id) REFERENCES loja (id),
  FOREIGN KEY (material_id) REFERENCES material (id),
  FOREIGN KEY (modelo_id) REFERENCES modelo (id),
  FOREIGN KEY (item_id) REFERENCES item (id),
  FOREIGN KEY (tamanho_id) REFERENCES tamanho (id),
  FOREIGN KEY (tipo_id) REFERENCES tipo (id),
  FOREIGN KEY (faixa_etaria_id) REFERENCES faixa_etaria (id),
  FOREIGN KEY (operacao_id) REFERENCES operacao (id),
  FOREIGN KEY (estado_id) REFERENCES estado (id)
);