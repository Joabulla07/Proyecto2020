CREATE SCHEMA IF NOT EXISTS `proyecto_info` DEFAULT CHARACTER SET latin1 COLLATE latin1_bin 
CREATE TABLE IF NOT EXISTS `proyecto_info`.`pacientes` (
  `idpacientes` INT NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `dni` CHAR(8) NOT NULL,
  `domicilio` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idpacientes`, `nombres`, `apellidos`, `dni`, `domicilio`, `correo`, `telefono`))
ENGINE = InnoDB
INSERT INTO `proyecto_info`.`pacientes` (`nombres`, `apellidos`, `dni`, `domicilio`, `correo`, `telefono`)
VALUES ('Franco Luciano', 'Maksimchuk Castillo', '42263243', 'Lisandro de la Torre 425', 'francolucastillo@gmail.com', '+543624689890')