CREATE DATABASE db_visu;

USE db_visu;

CREATE TABLE `unite` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `numero` int unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `automate` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `reference_type` varchar(50) NOT NULL,
  `id_unite` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT FOREIGN KEY (`id_unite`) REFERENCES `unite` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `donnee_mesuree` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `valeur` double DEFAULT NULL,
  `unite_mesure` varchar(50) DEFAULT NULL,
  `date_heure` datetime DEFAULT NOW(),
  `id_automate` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT FOREIGN KEY (`id_automate`) REFERENCES `automate` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `fichier` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `poid` float NOT NULL,
  `date_heure_creation` datetime DEFAULT NOW(),
  `date_heure_envoi` datetime DEFAULT NOW(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `utilisateur` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `login` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `profil`varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `unite`(`numero`) values
(1),
(2),
(3),
(4),
(5);

insert into `automate` (`reference_type`,`id_unite`) values ('0X0000BA20',1), ('0X0000BA21',1), ('0X0000BA22',1), ('0X0000BA23',1), ('0X0000BA24',1), ('0X0000BA25',1), ('0X0000BA26',1), ('0X0000BA27',1), ('0X0000BA28',1), ('0X0000BA29',1),
('0X0000BA20',2), ('0X0000BA21',2), ('0X0000BA22',2), ('0X0000BA23',2), ('0X0000BA24',2), ('0X0000BA25',2), ('0X0000BA26',2), ('0X0000BA27',2), ('0X0000BA28',2),('0X0000BA29',2),
('0X0000BA20',3), ('0X0000BA21',3), ('0X0000BA22',3), ('0X0000BA23',3), ('0X0000BA24',3), ('0X0000BA25',3), ('0X0000BA26',3), ('0X0000BA27',3), ('0X0000BA28',3), ('0X0000BA29',3),
('0X0000BA20',4), ('0X0000BA21',4), ('0X0000BA22',4), ('0X0000BA23',4), ('0X0000BA24',4), ('0X0000BA25',4), ('0X0000BA26',4), ('0X0000BA27',4), ('0X0000BA28',4), ('0X0000BA29',4),
('0X0000BA20',5), ('0X0000BA21',5), ('0X0000BA22',5), ('0X0000BA23',5), ('0X0000BA24',5), ('0X0000BA25',5), ('0X0000BA26',5), ('0X0000BA27',5), ('0X0000BA28',5), ('0X0000BA29',5);
