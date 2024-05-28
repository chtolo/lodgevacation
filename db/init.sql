CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

CREATE TABLE IF NOT EXISTS user (
    userid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS reservation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    nom_maison VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    nombre_personnes INT NOT NULL,
    nombre_nuits INT NOT NULL,
    FOREIGN KEY (email) REFERENCES user(email)
);

-- Insérez quelques données de test
INSERT INTO user (name, email, password) VALUES ('salma', 'salma@email.com', 'password123'), ('Bob', 'bob@example.com', 'password456');
INSERT INTO reservation (email, nom_maison, date, nombre_personnes, nombre_nuits) VALUES ('alice@example.com', 'Maison de Alice', '2024-06-01', 4, 3), ('bob@example.com', 'Maison de Bob', '2024-06-10', 2, 2);
