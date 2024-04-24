CREATE DATABASE oop_python DEFAULT CHARACTER SET = 'utf8mb4';

USE oop_python;

CREATE TABLE dosen(  
    id_dosen    INTEGER(11) NOT NULL AUTO_INCREMENT,
    nama_dosen  VARCHAR(50) NOT NULL,
    no_telp     VARCHAR(13),
    email       VARCHAR(30) NOT NULL,
    password    VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_dosen),
    UNIQUE (email)
);

INSERT INTO dosen VALUES
('1', 'Aisyah Hasanah, S.Pd', '088811188811', 'aisyah@example.com', 'password');

CREATE TABLE siswa(  
    id_siswa    INTEGER(11) NOT NULL AUTO_INCREMENT,
    id_dosen    INTEGER(11) NOT NULL,
    nama_siswa  VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_siswa),
    FOREIGN KEY (id_dosen) REFERENCES dosen(id_dosen)
);

INSERT INTO siswa VALUES
('1', '1', 'Humaira Santoso'),
('2', '1', 'Hesti Sirait'),
('3', '1', 'Dadap Mardhiyah'),
('4', '1', 'Mahfud Anggraini'),
('5', '1', 'Respati Marpaung'),
('6', '1', 'Wirda Waskita'),
('7', '1', 'Vega Mardhiyah'),
('8', '1', 'Latika Pradana'),
('9', '1', 'Cornelia Mardhiyah'),
('10', '1', 'Yuliana Putra'),
('11', '1', 'Ami Sitompul'),
('12', '1', 'Cakrawangsa Nashiruddin'),
('13', '1', 'Keisha Rahmawati'),
('14', '1', 'Caturangga Suwarno'),
('15', '1', 'Nova Kusumo');