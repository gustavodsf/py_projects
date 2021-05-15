--INSERT INTO colecao(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO cor(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO faixa_etaria(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO genero(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO loja(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO material(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO modelo(nome, pattern)VALUES (?, ?, ?);
--INSERT INTO tamanho(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO tipo(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO item(id, nome, tipo, pattern)VALUES (?, ?, ?, ?);
--INSERT INTO estado(id, nome, pattern)VALUES (?, ?, ?);
--INSERT INTO operacao(id, nome, pattern)VALUES (?, ?, ?);

--
--Faixa Etaria
--
INSERT INTO faixa_etaria(nome, pattern)VALUES ('Infantil', 'INF');
INSERT INTO faixa_etaria(nome, pattern)VALUES ('Adulto', 'AD');

--
-- Loja A
--
INSERT INTO loja(nome, pattern)VALUES ('Loja-Boa', '0');
INSERT INTO loja(nome, pattern)VALUES ('Loja-Ruim', '1');

--
-- Estado
--
INSERT INTO estado(nome, pattern)VALUES ('Normal', 'NORMAL');
INSERT INTO estado(nome, pattern)VALUES ('Desconto', 'DESCONTO');
INSERT INTO estado(nome, pattern)VALUES ('Promoção', 'PROMOCIONAL');
INSERT INTO estado(nome, pattern)VALUES ('Promoção', 'PROMOCAO');
INSERT INTO estado(nome, pattern)VALUES ('Mostruário', 'MOSTRUÁRIO');

--
-- Operacao
--
INSERT INTO operacao(nome, pattern)VALUES ('Venda', 'VENDA MERCADORIA');
INSERT INTO operacao(nome, pattern)VALUES ('Transferência', 'TRANSFERENCIA PARA COMERCIALIZAÇÃO');
INSERT INTO operacao(nome, pattern)VALUES ('Devolução', 'DEVOLUÇÃO DE VENDA');



---
--- Coleção
---
INSERT INTO colecao(nome, pattern)VALUES ('Verão/2012', 'VER 012');
INSERT INTO colecao(nome, pattern)VALUES ('Verão/2013', 'VER 013');
INSERT INTO colecao(nome, pattern)VALUES ('Verão/2014', 'VER 014');

INSERT INTO colecao(nome, pattern)VALUES ('Inverno/2012', 'INV 012');
INSERT INTO colecao(nome, pattern)VALUES ('Inverno/2013', 'INV 013');
INSERT INTO colecao(nome, pattern)VALUES ('Inverno/2014', 'INV 014');
INSERT INTO colecao(nome, pattern)VALUES ('AV', 'AV');

--
-- Tipo
--
INSERT INTO tipo(nome, pattern)VALUES ('Calçado', 'CALCADO');
INSERT INTO tipo(nome, pattern)VALUES ('Acessório', 'ACESSORIO');
INSERT INTO tipo(nome, pattern)VALUES ('Roupa - Above HIP', 'ABOVEHIP');
INSERT INTO tipo(nome, pattern)VALUES ('Roupa - Below Hip', 'BELOWHIP');

--
-- Genero
--
INSERT INTO genero(nome, pattern)VALUES ('Masculino','MASC');
INSERT INTO genero(nome, pattern)VALUES ('Feminino' ,'FEM');
INSERT INTO genero(nome, pattern)VALUES ('Unisex' ,'UNISEX');

--
-- Tamanho
--
INSERT INTO tamanho(nome, pattern)VALUES ('PP','PP');
INSERT INTO tamanho(nome, pattern)VALUES ('P','P');
INSERT INTO tamanho(nome, pattern)VALUES ('M','M');
INSERT INTO tamanho(nome, pattern)VALUES ('G','G');
INSERT INTO tamanho(nome, pattern)VALUES ('GG','GG');
INSERT INTO tamanho(nome, pattern)VALUES ('Único','UN');
INSERT INTO tamanho(nome, pattern)VALUES ('EXPP','EXPP');
INSERT INTO tamanho(nome, pattern)VALUES ('EXGG','EXGG');
INSERT INTO tamanho(nome, pattern)VALUES ('EXG','EXG');
INSERT INTO tamanho(nome, pattern)VALUES ('Pequena','PQ');
INSERT INTO tamanho(nome, pattern)VALUES ('Pequena','PEQUENA');
INSERT INTO tamanho(nome, pattern)VALUES ('Grande','GRANDE');
INSERT INTO tamanho(nome, pattern)VALUES ('Grande','GR');
INSERT INTO tamanho(nome, pattern)VALUES ('XG','XG');

---
--- Material
---
INSERT INTO material(nome, pattern)VALUES ('Algodão', 'ALGODAO');
INSERT INTO material(nome, pattern)VALUES ('Jeans','JEANS');
INSERT INTO material(nome, pattern)VALUES ('Microfibra','MICROFIBRA');
INSERT INTO material(nome, pattern)VALUES ('Stretch','STRETCH');
INSERT INTO material(nome, pattern)VALUES ('Rip','RIP');
INSERT INTO material(nome, pattern)VALUES ('Stop','STOP');
INSERT INTO material(nome, pattern)VALUES ('Sarja','SARJA');
INSERT INTO material(nome, pattern)VALUES ('Peletizado','PELETIZADO');
INSERT INTO material(nome, pattern)VALUES ('Malha','MALHA');
INSERT INTO material(nome, pattern)VALUES ('Diversos','DIVERSOS');
INSERT INTO material(nome, pattern)VALUES ('Nylon','NYLON');
INSERT INTO material(nome, pattern)VALUES ('Lycra','LYCRA');
INSERT INTO material(nome, pattern)VALUES ('Flame','FLAME');
INSERT INTO material(nome, pattern)VALUES ('Sintético','SINTETICO');
INSERT INTO material(nome, pattern)VALUES ('Lona','LONA');
INSERT INTO material(nome, pattern)VALUES ('Tecido','TECIDO');
INSERT INTO material(nome, pattern)VALUES ('Couro','COURO');
INSERT INTO material(nome, pattern)VALUES ('Ribana','RIBANA');
INSERT INTO material(nome, pattern)VALUES ('Plástico','PLASTICO');
INSERT INTO material(nome, pattern)VALUES ('Moleton','MOLETON');
INSERT INTO material(nome, pattern)VALUES ('Lurex','LUREX');
INSERT INTO material(nome, pattern)VALUES ('Neoprene','NEOPRENE');
INSERT INTO material(nome, pattern)VALUES ('Metal','METAL');
INSERT INTO material(nome, pattern)VALUES ('Viscolycra','VISCOLYCRA');
INSERT INTO material(nome, pattern)VALUES ('Resina','RESINA');
INSERT INTO material(nome, pattern)VALUES ('Poliéster','POLIESTER');
INSERT INTO material(nome, pattern)VALUES ('Poliuretano','POLIURETANO');
INSERT INTO material(nome, pattern)VALUES ('Brim','BRIM');
INSERT INTO material(nome, pattern)VALUES ('Viscose','VISCOSE');
INSERT INTO material(nome, pattern)VALUES ('Madeira','MADEIRA');
INSERT INTO material(nome, pattern)VALUES ('Cotton','COTTON');
INSERT INTO material(nome, pattern)VALUES ('Papel','PAPEL');
INSERT INTO material(nome, pattern)VALUES ('Cetim','CETIM');
INSERT INTO material(nome, pattern)VALUES ('Cordoba','CORDOBA');
INSERT INTO material(nome, pattern)VALUES ('Camurça','CAMURCA');
INSERT INTO material(nome, pattern)VALUES ('Tricoline','TRICOLINE');
INSERT INTO material(nome, pattern)VALUES ('Lesie','LESIE');
INSERT INTO material(nome, pattern)VALUES ('Pedra','PEDRA');
INSERT INTO material(nome, pattern)VALUES ('Misto','MISTO');
INSERT INTO material(nome, pattern)VALUES ('Cera','CERA');

--
-- Modelo
--
INSERT INTO modelo(nome, pattern)VALUES ('Baby','BABY');
INSERT INTO modelo(nome, pattern)VALUES ('Look','LOOK');
INSERT INTO modelo(nome, pattern)VALUES ('Camberra','CAMBERRA');
INSERT INTO modelo(nome, pattern)VALUES ('Gola','GOLA');
INSERT INTO modelo(nome, pattern)VALUES ('V','V');
INSERT INTO modelo(nome, pattern)VALUES ('Básica','BASICA');
INSERT INTO modelo(nome, pattern)VALUES ('Curta','CURTA');
INSERT INTO modelo(nome, pattern)VALUES ('Invisível','INVISIVEL');
INSERT INTO modelo(nome, pattern)VALUES ('Box','BOX');
INSERT INTO modelo(nome, pattern)VALUES ('Viagem','VIAGEM');
INSERT INTO modelo(nome, pattern)VALUES ('Longa','LONGA');
INSERT INTO modelo(nome, pattern)VALUES ('Pier','PIER');
INSERT INTO modelo(nome, pattern)VALUES ('Camping','CAMPING');
INSERT INTO modelo(nome, pattern)VALUES ('Slip','SLIP');
INSERT INTO modelo(nome, pattern)VALUES ('Rasta','RASTA');
INSERT INTO modelo(nome, pattern)VALUES ('Out','OUT');
INSERT INTO modelo(nome, pattern)VALUES ('Halls','HALLS');
INSERT INTO modelo(nome, pattern)VALUES ('Trident','TRIDENT');
INSERT INTO modelo(nome, pattern)VALUES ('Picolé','PICOLE');
INSERT INTO modelo(nome, pattern)VALUES ('Craquele','CRAQUELE');
INSERT INTO modelo(nome, pattern)VALUES ('Linha','LINHA');
INSERT INTO modelo(nome, pattern)VALUES ('Surfboards','SURFBOADS');
INSERT INTO modelo(nome, pattern)VALUES ('Academia','ACADEMIA');
INSERT INTO modelo(nome, pattern)VALUES ('Futebol','FUTEBOL');
INSERT INTO modelo(nome, pattern)VALUES ('Manga','MANGA');
INSERT INTO modelo(nome, pattern)VALUES ('Squeeze','SQUEEZE');
INSERT INTO modelo(nome, pattern)VALUES ('Prancha','PRANCHA');
INSERT INTO modelo(nome, pattern)VALUES ('Copa','COPA');
INSERT INTO modelo(nome, pattern)VALUES ('Surf','SURF');
INSERT INTO modelo(nome, pattern)VALUES ('Frente','FRENTE');
INSERT INTO modelo(nome, pattern)VALUES ('Logo','LOGO');
INSERT INTO modelo(nome, pattern)VALUES ('LG','LG');
INSERT INTO modelo(nome, pattern)VALUES ('Encerada','ENCERADA');
INSERT INTO modelo(nome, pattern)VALUES ('Viés','VIES');
INSERT INTO modelo(nome, pattern)VALUES ('Dartbag','DARTBAG');
INSERT INTO modelo(nome, pattern)VALUES ('Estanque','ESTANQUE');
INSERT INTO modelo(nome, pattern)VALUES ('Flúor','FLUOR');
INSERT INTO modelo(nome, pattern)VALUES ('Renda','RENDA');
INSERT INTO modelo(nome, pattern)VALUES ('Ombro','OMBRO');
INSERT INTO modelo(nome, pattern)VALUES ('Jamaica','JAMAICA');
INSERT INTO modelo(nome, pattern)VALUES ('Costas','COSTAS');
INSERT INTO modelo(nome, pattern)VALUES ('Mágica','MÁGICA');
INSERT INTO modelo(nome, pattern)VALUES ('Câmera','CÂMERA');
INSERT INTO modelo(nome, pattern)VALUES ('Viés','VIÉS');
INSERT INTO modelo(nome, pattern)VALUES ('Canoa','CANOA');
INSERT INTO modelo(nome, pattern)VALUES ('Fusca','FUSCA');
INSERT INTO modelo(nome, pattern)VALUES ('Coração','CORAÇÃO');
INSERT INTO modelo(nome, pattern)VALUES ('Estrelas','ESTRELAS');
INSERT INTO modelo(nome, pattern)VALUES ('Road','ROAD');
INSERT INTO modelo(nome, pattern)VALUES ('Capuz','CAPUZ');
INSERT INTO modelo(nome, pattern)VALUES ('Trips','TRIPS');
INSERT INTO modelo(nome, pattern)VALUES ('Ipanema','IPANEMA');
INSERT INTO modelo(nome, pattern)VALUES ('Recorte','RECORTE');
INSERT INTO modelo(nome, pattern)VALUES ('Aberta','ABERTA');
INSERT INTO modelo(nome, pattern)VALUES ('Máquinas','MAQUINAS');
INSERT INTO modelo(nome, pattern)VALUES ('Militar','MILITAR');
INSERT INTO modelo(nome, pattern)VALUES ('Gin','GIN');
INSERT INTO modelo(nome, pattern)VALUES ('Elástico','ELASTICO');
INSERT INTO modelo(nome, pattern)VALUES ('Alta','ALTA');
INSERT INTO modelo(nome, pattern)VALUES ('MMA','MMA');
INSERT INTO modelo(nome, pattern)VALUES ('Simples','SIMPLES');
INSERT INTO modelo(nome, pattern)VALUES ('Flor','FLOR');
INSERT INTO modelo(nome, pattern)VALUES ('Paete','PAETE');
INSERT INTO modelo(nome, pattern)VALUES ('Passeio','PASSEIO');
INSERT INTO modelo(nome, pattern)VALUES ('Trabalhado','TRABALHADO');
INSERT INTO modelo(nome, pattern)VALUES ('Longo','LONGO');
INSERT INTO modelo(nome, pattern)VALUES ('Esportivo','ESPORTIVO');
INSERT INTO modelo(nome, pattern)VALUES ('Fecho','FECHO');
INSERT INTO modelo(nome, pattern)VALUES ('Transpbolso','TRANSPBOLSO');
INSERT INTO modelo(nome, pattern)VALUES ('Carteiro','CARTEIRO');
INSERT INTO modelo(nome, pattern)VALUES ('Chiclets','CHICLETS');
INSERT INTO modelo(nome, pattern)VALUES ('Bike','BIKE');
INSERT INTO modelo(nome, pattern)VALUES ('Tela','TELA');
INSERT INTO modelo(nome, pattern)VALUES ('Cadarço','CADARÇO');
INSERT INTO modelo(nome, pattern)VALUES ('Máqina','MAQUINA');
INSERT INTO modelo(nome, pattern)VALUES ('Asa','ASA');
INSERT INTO modelo(nome, pattern)VALUES ('Woman','WOMAN');
INSERT INTO modelo(nome, pattern)VALUES ('Polarizado','POLARIZADO');
INSERT INTO modelo(nome, pattern)VALUES ('Fita','FITA');
INSERT INTO modelo(nome, pattern)VALUES ('Ziper','ZIPER');
INSERT INTO modelo(nome, pattern)VALUES ('240 ml','240 ML');
INSERT INTO modelo(nome, pattern)VALUES ('Sapo','SAPO');
INSERT INTO modelo(nome, pattern)VALUES ('Babado','BABADO');
INSERT INTO modelo(nome, pattern)VALUES ('Difer','DIFER');
INSERT INTO modelo(nome, pattern)VALUES ('Fer','FER');
INSERT INTO modelo(nome, pattern)VALUES ('Porta','PORTA');
INSERT INTO modelo(nome, pattern)VALUES ('MG','MG');
INSERT INTO modelo(nome, pattern)VALUES ('Dupla','DUPLA');
INSERT INTO modelo(nome, pattern)VALUES ('Tigre','TIGRE');
INSERT INTO modelo(nome, pattern)VALUES ('Bolso','BOLSO');
INSERT INTO modelo(nome, pattern)VALUES ('Surfista','SURFISTA');
INSERT INTO modelo(nome, pattern)VALUES ('Camguru','CANGURU');
INSERT INTO modelo(nome, pattern)VALUES ('Avião','AVIÃO');
INSERT INTO modelo(nome, pattern)VALUES ('Acrobacia','ACROBACIA');
INSERT INTO modelo(nome, pattern)VALUES ('Borboleta','BORBOLETA');
INSERT INTO modelo(nome, pattern)VALUES ('Point','POINT');
INSERT INTO modelo(nome, pattern)VALUES ('Faixas','FAIXAS');
INSERT INTO modelo(nome, pattern)VALUES ('Franja','FRANJA');
INSERT INTO modelo(nome, pattern)VALUES ('Gato','GATO');
INSERT INTO modelo(nome, pattern)VALUES ('Pug','PUG');
INSERT INTO modelo(nome, pattern)VALUES ('Xadrez','XADREZ');
INSERT INTO modelo(nome, pattern)VALUES ('Praia','PRAIA');
INSERT INTO modelo(nome, pattern)VALUES ('Celular','CELULAR');
INSERT INTO modelo(nome, pattern)VALUES ('Hawai','HAWAI');
INSERT INTO modelo(nome, pattern)VALUES ('Montaria','MONTARIA');
INSERT INTO modelo(nome, pattern)VALUES ('Coqueiro','COQUEIRO');
INSERT INTO modelo(nome, pattern)VALUES ('Flores','FLORES');
INSERT INTO modelo(nome, pattern)VALUES ('Acetato','ACETATO');
INSERT INTO modelo(nome, pattern)VALUES ('Peruana','PERUANA');
INSERT INTO modelo(nome, pattern)VALUES ('Lateral','LATERAL');
INSERT INTO modelo(nome, pattern)VALUES ('Guitarra','GUITARRA');
INSERT INTO modelo(nome, pattern)VALUES ('Biscoito','BISCOITO');
INSERT INTO modelo(nome, pattern)VALUES ('Básico','BASICO');
INSERT INTO modelo(nome, pattern)VALUES ('Cup','CUP');
INSERT INTO modelo(nome, pattern)VALUES ('Tule','TULE');
INSERT INTO modelo(nome, pattern)VALUES ('Cake','CAKE');
INSERT INTO modelo(nome, pattern)VALUES ('Curto','CURTO');
INSERT INTO modelo(nome, pattern)VALUES ('Placa','PLACA');
INSERT INTO modelo(nome, pattern)VALUES ('Malhão','MALHÃO');
INSERT INTO modelo(nome, pattern)VALUES ('Pregas','PREGAS');
INSERT INTO modelo(nome, pattern)VALUES ('Roma','ROMA');
INSERT INTO modelo(nome, pattern)VALUES ('Velcro','VELCRO');
INSERT INTO modelo(nome, pattern)VALUES ('Com botão','C/BOTÃO');
INSERT INTO modelo(nome, pattern)VALUES ('Estampado','ESTAMPADO');
INSERT INTO modelo(nome, pattern)VALUES ('Liso','LISO');
INSERT INTO modelo(nome, pattern)VALUES ('Croo','CARRO');
INSERT INTO modelo(nome, pattern)VALUES ('OXFORD','OXFORD');
INSERT INTO modelo(nome, pattern)VALUES ('Mecha','MECHA');
INSERT INTO modelo(nome, pattern)VALUES ('Hip','HIP');
INSERT INTO modelo(nome, pattern)VALUES ('Laptop','LAPTOP');
INSERT INTO modelo(nome, pattern)VALUES ('Rabo','RABO');
INSERT INTO modelo(nome, pattern)VALUES ('Pro','PRO');
INSERT INTO modelo(nome, pattern)VALUES ('Feira','FEIRA');
INSERT INTO modelo(nome, pattern)VALUES ('POA','POA');
INSERT INTO modelo(nome, pattern)VALUES ('Costa','COSTA');
INSERT INTO modelo(nome, pattern)VALUES ('Floral','FLORAL');
INSERT INTO modelo(nome, pattern)VALUES ('Tubinho','TUBINHO');
INSERT INTO modelo(nome, pattern)VALUES ('TQC','TQC');
INSERT INTO modelo(nome, pattern)VALUES ('Dia','DIA');
INSERT INTO modelo(nome, pattern)VALUES ('Social','SOCIAL');
INSERT INTO modelo(nome, pattern)VALUES ('Borrachada','BORRACHADA');
INSERT INTO modelo(nome, pattern)VALUES ('Fish','FISH');
INSERT INTO modelo(nome, pattern)VALUES ('Fechado','FECHADO');
INSERT INTO modelo(nome, pattern)VALUES ('Sem Capuz','S/CAPUZ');
INSERT INTO modelo(nome, pattern)VALUES ('Padle','PADLE');
INSERT INTO modelo(nome, pattern)VALUES ('New','NEW');
INSERT INTO modelo(nome, pattern)VALUES ('Drapeado','DRAPEADO');
INSERT INTO modelo(nome, pattern)VALUES ('TCQ','TCQ');
INSERT INTO modelo(nome, pattern)VALUES ('Violão','VIOLAO');
INSERT INTO modelo(nome, pattern)VALUES ('Cartão','CARTÃO');
INSERT INTO modelo(nome, pattern)VALUES ('Morcego','MORCEGO');
INSERT INTO modelo(nome, pattern)VALUES ('Amizade','AMIZADE');
INSERT INTO modelo(nome, pattern)VALUES ('Franzido','FRANZIDO');
INSERT INTO modelo(nome, pattern)VALUES ('Com Tule','C/TULE');
INSERT INTO modelo(nome, pattern)VALUES ('Redonda','REDONDA');
INSERT INTO modelo(nome, pattern)VALUES ('Camadas','CAMADAS');
INSERT INTO modelo(nome, pattern)VALUES ('Jardineiro','JARDINEIRO');
INSERT INTO modelo(nome, pattern)VALUES ('Lisa','LISA');
INSERT INTO modelo(nome, pattern)VALUES ('Long','LONG');
INSERT INTO modelo(nome, pattern)VALUES ('Câmera','CAMERA');
INSERT INTO modelo(nome, pattern)VALUES ('BER','BER');
INSERT INTO modelo(nome, pattern)VALUES ('Ala','ALA');
INSERT INTO modelo(nome, pattern)VALUES ('Nadador','NADADOR');
INSERT INTO modelo(nome, pattern)VALUES ('Combi','COMBI');
INSERT INTO modelo(nome, pattern)VALUES ('Retro','RETRO');
INSERT INTO modelo(nome, pattern)VALUES ('Soft','SOFT');
INSERT INTO modelo(nome, pattern)VALUES ('Envelope','ENVELOPE');
INSERT INTO modelo(nome, pattern)VALUES ('Sungão','SUNGAO');
INSERT INTO modelo(nome, pattern)VALUES ('Place','PLACE');
INSERT INTO modelo(nome, pattern)VALUES ('Five','FIVE');
INSERT INTO modelo(nome, pattern)VALUES ('Com dourado','C/DOURADO');
INSERT INTO modelo(nome, pattern)VALUES ('Lastex','LASTEX');
INSERT INTO modelo(nome, pattern)VALUES ('Days','DAYS');
INSERT INTO modelo(nome, pattern)VALUES ('Gabriela','GABRIELA');
INSERT INTO modelo(nome, pattern)VALUES ('Bordado','BORDADO');
INSERT INTO modelo(nome, pattern)VALUES ('Banda','BANDA');
INSERT INTO modelo(nome, pattern)VALUES ('Laço','LAÇO');
INSERT INTO modelo(nome, pattern)VALUES ('Bola','BOLA');
INSERT INTO modelo(nome, pattern)VALUES ('Cruz','CRUZ');
INSERT INTO modelo(nome, pattern)VALUES ('Regatão','REGATÃO');
INSERT INTO modelo(nome, pattern)VALUES ('Detalhe','DETALHE');
INSERT INTO modelo(nome, pattern)VALUES ('Individual','INDIVIDUAL');
INSERT INTO modelo(nome, pattern)VALUES ('Mista','MISTA');
INSERT INTO modelo(nome, pattern)VALUES ('Busto','BUSTO');
INSERT INTO modelo(nome, pattern)VALUES ('Tribal','TRIBAL');
INSERT INTO modelo(nome, pattern)VALUES ('Prega','PREGA');
INSERT INTO modelo(nome, pattern)VALUES ('Paz','PAZ');
INSERT INTO modelo(nome, pattern)VALUES ('Bordada','BORDADA');
INSERT INTO modelo(nome, pattern)VALUES ('Gatinho','GATINHO');
INSERT INTO modelo(nome, pattern)VALUES ('Cadarço','CADARCO');
INSERT INTO modelo(nome, pattern)VALUES ('Argola','ARGOLA');
INSERT INTO modelo(nome, pattern)VALUES ('Naine','NAINE');
INSERT INTO modelo(nome, pattern)VALUES ('Bueno','BUENO');
INSERT INTO modelo(nome, pattern)VALUES ('Proteção','PROTEÇÃO');
INSERT INTO modelo(nome, pattern)VALUES ('Color','COLOR');
INSERT INTO modelo(nome, pattern)VALUES ('Bord','BORD');
INSERT INTO modelo(nome, pattern)VALUES ('Fresado','FRESADO');
INSERT INTO modelo(nome, pattern)VALUES ('Soho','SOHO');
INSERT INTO modelo(nome, pattern)VALUES ('Colorida','COLORIDA');
INSERT INTO modelo(nome, pattern)VALUES ('Fino','FINO');
INSERT INTO modelo(nome, pattern)VALUES ('Tablet','TABLET');
INSERT INTO modelo(nome, pattern)VALUES ('Gripir','GRIPIR');
INSERT INTO modelo(nome, pattern)VALUES ('Sector','SECTOR');
INSERT INTO modelo(nome, pattern)VALUES ('Baton','BATON');
INSERT INTO modelo(nome, pattern)VALUES ('Havana','HAVANA');
INSERT INTO modelo(nome, pattern)VALUES ('Sorte','SORTE');
INSERT INTO modelo(nome, pattern)VALUES ('Grippy','GRIPPY');
INSERT INTO modelo(nome, pattern)VALUES ('Surf','SURFE');
INSERT INTO modelo(nome, pattern)VALUES ('Com Couro','C/COURO');
INSERT INTO modelo(nome, pattern)VALUES ('Nina','NINA');
INSERT INTO modelo(nome, pattern)VALUES ('Coberto','COBERTO');
INSERT INTO modelo(nome, pattern)VALUES ('Sobreposição','SOBREPOSIÇÃO');
INSERT INTO modelo(nome, pattern)VALUES ('Bojo','BOJO');
INSERT INTO modelo(nome, pattern)VALUES ('Mini','MINI');
INSERT INTO modelo(nome, pattern)VALUES ('Babados','BABADOS');
INSERT INTO modelo(nome, pattern)VALUES ('Listra','LISTRA');
INSERT INTO modelo(nome, pattern)VALUES ('Multi','MULTI');
INSERT INTO modelo(nome, pattern)VALUES ('Tecnologic','TECNOLOGIC');
INSERT INTO modelo(nome, pattern)VALUES ('Camis','CAMIS');
INSERT INTO modelo(nome, pattern)VALUES ('Semi','SEMI');
INSERT INTO modelo(nome, pattern)VALUES ('Est.','EST');
INSERT INTO modelo(nome, pattern)VALUES ('Estrela','ESTRELA');
INSERT INTO modelo(nome, pattern)VALUES ('Litra','LITRA');
INSERT INTO modelo(nome, pattern)VALUES ('Girassol','GIRASOL');
INSERT INTO modelo(nome, pattern)VALUES ('Bicicleta','BICICLETA');
INSERT INTO modelo(nome, pattern)VALUES ('Tricot.','TRICOT');
INSERT INTO modelo(nome, pattern)VALUES ('Laco','LACO');
INSERT INTO modelo(nome, pattern)VALUES ('Sino','SINO');
INSERT INTO modelo(nome, pattern)VALUES ('BAS','BAS');
INSERT INTO modelo(nome, pattern)VALUES ('Horizontal','HORIZONTAL');
INSERT INTO modelo(nome, pattern)VALUES ('Profissional','PROFISSIONAL');
INSERT INTO modelo(nome, pattern)VALUES ('Aleixo','ALEIXO');
INSERT INTO modelo(nome, pattern)VALUES ('Metálico','METALICO');
INSERT INTO modelo(nome, pattern)VALUES ('Amarração','AMARRAÇÃO');
INSERT INTO modelo(nome, pattern)VALUES ('South','SOUTH');
INSERT INTO modelo(nome, pattern)VALUES ('Randa','RANDA');
INSERT INTO modelo(nome, pattern)VALUES ('Stand','STAND');
INSERT INTO modelo(nome, pattern)VALUES ('Pontas','PONTAS');
INSERT INTO modelo(nome, pattern)VALUES ('Tomara','TOMARA');
INSERT INTO modelo(nome, pattern)VALUES ('Cachorro','CACHORRO');
INSERT INTO modelo(nome, pattern)VALUES ('Face','FACE');
INSERT INTO modelo(nome, pattern)VALUES ('POrtátil','PORTATIL');
INSERT INTO modelo(nome, pattern)VALUES ('Faixa','FAIXA');
INSERT INTO modelo(nome, pattern)VALUES ('Com Detalhe','C/DETALHE');
INSERT INTO modelo(nome, pattern)VALUES ('Decote','DECOTE');
INSERT INTO modelo(nome, pattern)VALUES ('Quadrado','QUADRADO');
INSERT INTO modelo(nome, pattern)VALUES ('Três','TRES');
INSERT INTO modelo(nome, pattern)VALUES ('Meio','MEIO');
INSERT INTO modelo(nome, pattern)VALUES ('Dist.','DIST');
INSERT INTO modelo(nome, pattern)VALUES ('Radical','RADICAL');
INSERT INTO modelo(nome, pattern)VALUES ('Com Massa','C/MASSA');
INSERT INTO modelo(nome, pattern)VALUES ('Bolsinha','BOLSINHA');
INSERT INTO modelo(nome, pattern)VALUES ('Lasie','LASIE');
INSERT INTO modelo(nome, pattern)VALUES ('Mochi','MOCHI');
INSERT INTO modelo(nome, pattern)VALUES ('Boia','BOIA');
INSERT INTO modelo(nome, pattern)VALUES ('Up','UP');
INSERT INTO modelo(nome, pattern)VALUES ('Casulo','CASULO');
INSERT INTO modelo(nome, pattern)VALUES ('Fofa','FOFA');
INSERT INTO modelo(nome, pattern)VALUES ('Urban','URBAN');
INSERT INTO modelo(nome, pattern)VALUES ('Beach','BEACH');


---
--- Cor
---
INSERT INTO cor(nome, pattern)VALUES ('Única','UNICA');
INSERT INTO cor(nome, pattern)VALUES ('Branco','BRANCO');
INSERT INTO cor(nome, pattern)VALUES ('Preto','PRETO');
INSERT INTO cor(nome, pattern)VALUES ('Azul','AZUL');
INSERT INTO cor(nome, pattern)VALUES ('Verde','VERDE');
INSERT INTO cor(nome, pattern)VALUES ('Vermelho','VERMELHO');
INSERT INTO cor(nome, pattern)VALUES ('Cinza','CINZA');
INSERT INTO cor(nome, pattern)VALUES ('Amarelo','AMARELO');
INSERT INTO cor(nome, pattern)VALUES ('Rosa','ROSA');
INSERT INTO cor(nome, pattern)VALUES ('Claro','CLARO');
INSERT INTO cor(nome, pattern)VALUES ('Marinho','MARINHO');
INSERT INTO cor(nome, pattern)VALUES ('Bege','BEGE');
INSERT INTO cor(nome, pattern)VALUES ('Petróleo','PETROLEO');
INSERT INTO cor(nome, pattern)VALUES ('Caki','CAKI');
INSERT INTO cor(nome, pattern)VALUES ('Gelo','GELO');
INSERT INTO cor(nome, pattern)VALUES ('Laranja','LARANJA');
INSERT INTO cor(nome, pattern)VALUES ('Bordo','BORDO');
INSERT INTO cor(nome, pattern)VALUES ('Grafite','GRAFITE');
INSERT INTO cor(nome, pattern)VALUES ('Musgo','MUSGO');
INSERT INTO cor(nome, pattern)VALUES ('Cimento','CIMENTO');
INSERT INTO cor(nome, pattern)VALUES ('Melância','MELANCIA');
INSERT INTO cor(nome, pattern)VALUES ('Salmon','SALMON');
INSERT INTO cor(nome, pattern)VALUES ('Chumbo','CHUMBO');
INSERT INTO cor(nome, pattern)VALUES ('Pistache','PISTACHE');
INSERT INTO cor(nome, pattern)VALUES ('Índigo','INDIGO');
INSERT INTO cor(nome, pattern)VALUES ('Marron','MARRON');
INSERT INTO cor(nome, pattern)VALUES ('Pink','PINK');
INSERT INTO cor(nome, pattern)VALUES ('Cobalto','COBALTO');
INSERT INTO cor(nome, pattern)VALUES ('Água','AGUA');
INSERT INTO cor(nome, pattern)VALUES ('Mostarda','MOSTARDA');
INSERT INTO cor(nome, pattern)VALUES ('BB','BB');
INSERT INTO cor(nome, pattern)VALUES ('Menta','MENTA');
INSERT INTO cor(nome, pattern)VALUES ('Vinho','VINHO');
INSERT INTO cor(nome, pattern)VALUES ('Crú','CRU');
INSERT INTO cor(nome, pattern)VALUES ('Prata','PRATA');
INSERT INTO cor(nome, pattern)VALUES ('Chino','CHINO');
INSERT INTO cor(nome, pattern)VALUES ('Mescla','MESCLA');
INSERT INTO cor(nome, pattern)VALUES ('Chocolate','CHOCOLATE');
INSERT INTO cor(nome, pattern)VALUES ('Telha','TELHA');
INSERT INTO cor(nome, pattern)VALUES ('Lilás','LILAS');
INSERT INTO cor(nome, pattern)VALUES ('Crepe','CREPE');
INSERT INTO cor(nome, pattern)VALUES ('Dourada','DOURADA');
INSERT INTO cor(nome, pattern)VALUES ('Trigo','TRIGO');
INSERT INTO cor(nome, pattern)VALUES ('Piscina','PISCINA');
INSERT INTO cor(nome, pattern)VALUES ('Lima','LIMA');
INSERT INTO cor(nome, pattern)VALUES ('Pastel','PASTEL');
INSERT INTO cor(nome, pattern)VALUES ('Ouro','OURO');
INSERT INTO cor(nome, pattern)VALUES ('Bandeira','BANDEIRA');
INSERT INTO cor(nome, pattern)VALUES ('Mineral','MINERAL');
INSERT INTO cor(nome, pattern)VALUES ('Café','CAFE');
INSERT INTO cor(nome, pattern)VALUES ('Areia','AREIA');
INSERT INTO cor(nome, pattern)VALUES ('Velho','VELHO');
INSERT INTO cor(nome, pattern)VALUES ('Marine','MARINE');
INSERT INTO cor(nome, pattern)VALUES ('Grená','GRENA');
INSERT INTO cor(nome, pattern)VALUES ('Cidra','CIDRA');
INSERT INTO cor(nome, pattern)VALUES ('Royal','ROYAL');
INSERT INTO cor(nome, pattern)VALUES ('Roxo','ROXO');
INSERT INTO cor(nome, pattern)VALUES ('Púrpura','PURPURA');
INSERT INTO cor(nome, pattern)VALUES ('Coral','CORAL');
INSERT INTO cor(nome, pattern)VALUES ('Pimenta','PIMENTA');
INSERT INTO cor(nome, pattern)VALUES ('Cor','COR');
INSERT INTO cor(nome, pattern)VALUES ('Jade','JADE');
INSERT INTO cor(nome, pattern)VALUES ('Bronze','BRONZE');
INSERT INTO cor(nome, pattern)VALUES ('Caribe','CARIBE');
INSERT INTO cor(nome, pattern)VALUES ('BIC','BIC');
INSERT INTO cor(nome, pattern)VALUES ('Rose','ROSE');
INSERT INTO cor(nome, pattern)VALUES ('Fumaça','FUMAÇA');
INSERT INTO cor(nome, pattern)VALUES ('Prestígio','PRESTIGIO');
INSERT INTO cor(nome, pattern)VALUES ('Cobre','COBRE');
INSERT INTO cor(nome, pattern)VALUES ('Ardósia','ARDOSIA');
INSERT INTO cor(nome, pattern)VALUES ('Pitange','PITANGA');
INSERT INTO cor(nome, pattern)VALUES ('Caramelo','CARAMELO');
INSERT INTO cor(nome, pattern)VALUES ('Cítrico','CITRICO');
INSERT INTO cor(nome, pattern)VALUES ('Lavanda','LAVANDA');
INSERT INTO cor(nome, pattern)VALUES ('Citrino','CITRINO');
INSERT INTO cor(nome, pattern)VALUES ('Mato','MATO');
INSERT INTO cor(nome, pattern)VALUES ('Azeitona','AZEITONA');
INSERT INTO cor(nome, pattern)VALUES ('Turquesa','TURQUESA');
INSERT INTO cor(nome, pattern)VALUES ('Cana','CANA');
INSERT INTO cor(nome, pattern)VALUES ('Acqua','ACQUA');
INSERT INTO cor(nome, pattern)VALUES ('Quartzo','QUARTZO');
INSERT INTO cor(nome, pattern)VALUES ('Maça','MAÇA');
INSERT INTO cor(nome, pattern)VALUES ('Marfim','MARFIM');



---
--- Item
---
INSERT INTO item(nome, tipo, pattern)VALUES ('Blazer','ABOVEHIP','BLAZER');
INSERT INTO item(nome, tipo, pattern)VALUES ('Colete','ABOVEHIP','COLETE');
INSERT INTO item(nome, tipo, pattern)VALUES ('Top','ABOVEHIP','TOP');
INSERT INTO item(nome, tipo, pattern)VALUES ('Macaquinho','ABOVEHIP','MACAQUINHO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Jaqueta','ABOVEHIP','JAQUETA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Casaquinho','ABOVEHIP','CASAQUINHO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Bolero','ABOVEHIP','BOLERO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Body','ABOVEHIP','BODY');
INSERT INTO item(nome, tipo, pattern)VALUES ('Casaqueto','ABOVEHIP','CASAQUETO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Camisão','ABOVEHIP','CAMISAO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Casaco','ABOVEHIP','CASACO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Blusa','ABOVEHIP','BLUSA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Polo','ABOVEHIP','POLO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Camisa','ABOVEHIP','CAMISA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Camiseta','ABOVEHIP','CAMISETA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Regata','ABOVEHIP','REGATA');
INSERT INTO item(nome, tipo, pattern)VALUES ('T-Shirt','ABOVEHIP','TSHIRT');
INSERT INTO item(nome, tipo, pattern)VALUES ('Vestido','ABOVEHIP','VESTIDO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Macacão','ABOVEHIP','MACACAO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Bermuda','BELOWHIP','BERMUDA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Short','BELOWHIP','SHORT');
INSERT INTO item(nome, tipo, pattern)VALUES ('Calça','BELOWHIP','CALÇA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Meia','BELOWHIP','MEIA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Sunga','BELOWHIP','SUNGA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Cueca','BELOWHIP','CUECA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Saia','BELOWHIP','SAIA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Bolsa','ACESSORIO','BOLSA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Doce','ACESSORIO','DOCE');
INSERT INTO item(nome, tipo, pattern)VALUES ('Carteira','ACESSORIO','CARTEIRA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Mochila','ACESSORIO','MOCHILA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Boné','ACESSORIO','BONE');
INSERT INTO item(nome, tipo, pattern)VALUES ('Cinto','ACESSORIO','CINTO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Borracha','ACESSORIO','BORRACHA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Chaveiro','ACESSORIO','CHAVEIRO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Ôculos','ACESSORIO','OCULOS');
INSERT INTO item(nome, tipo, pattern)VALUES ('Pulseira','ACESSORIO','PULSEIRA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Acessórios','ACESSORIO','ACESSORIOS');
INSERT INTO item(nome, tipo, pattern)VALUES ('Skate','ACESSORIO','SKATE');
INSERT INTO item(nome, tipo, pattern)VALUES ('Colar','ACESSORIO','COLAR');
INSERT INTO item(nome, tipo, pattern)VALUES ('Garrafa','ACESSORIO','GARRAFA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Mala','ACESSORIO','MALA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Brinco','ACESSORIO','BRINCO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Essência','ACESSORIO','ESSENCIA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Leash','ACESSORIO','LEASH');
INSERT INTO item(nome, tipo, pattern)VALUES ('pen-drive','ACESSORIO','PENDRIVE');
INSERT INTO item(nome, tipo, pattern)VALUES ('Chale','ACESSORIO','CHALE');
INSERT INTO item(nome, tipo, pattern)VALUES ('Gorro','ACESSORIO','GORRO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Arco de cabelo','ACESSORIO','ARCO DE CABELO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Pingente','ACESSORIO','PINGENTE');
INSERT INTO item(nome, tipo, pattern)VALUES ('Prancha de Fibra','ACESSORIO','PRANCHA FIBRA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Cartucheira','ACESSORIO','CARTUCHEIRA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Presilha','ACESSORIO','PRESILHA');
INSERT INTO item(nome, tipo, pattern)VALUES ('Cordão','ACESSORIO','CORDAO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Rack','ACESSORIO','RACK');
INSERT INTO item(nome, tipo, pattern)VALUES ('Caderno','ACESSORIO','CADERNO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Guarda Sol','ACESSORIO','GUARDA SOL');
INSERT INTO item(nome, tipo, pattern)VALUES ('Chinelo','CALCADO','CHINELO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Sapatênis','CALCADO','SAPATENIS');
INSERT INTO item(nome, tipo, pattern)VALUES ('Tênis','CALCADO','TENIS');
INSERT INTO item(nome, tipo, pattern)VALUES ('Sapato','CALCADO','SAPATO');
INSERT INTO item(nome, tipo, pattern)VALUES ('Deck','CALCADO','DECK');








