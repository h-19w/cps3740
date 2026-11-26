-- triggers
-- trigger an alert for certain commands like add/create/delete/anything\

DROP DATABASE IF EXISTS triggerdb;
CREATE DATABASE triggerdb;
USE triggerdb;

-- main table
CREATE TABLE tbluser (
    id         INT NOT NULL,
    `user`     VARCHAR(30),
    `password` VARCHAR(50),
    PRIMARY KEY (id)
);

-- history / audit table
-- history table (sno = auto row number)
CREATE TABLE IF NOT EXISTS oldtbluser (
    sno      INT AUTO_INCREMENT PRIMARY KEY,
    id       INT,
    user     VARCHAR(30),
    password VARCHAR(50)
);


SELECT * FROM TBLUSER;
SELECT* FROM OLDTBLUSER;


DELIMITER $$
CREATE TRIGGER userhistory
AFTER UPDATE ON tbluser
FOR EACH ROW
BEGIN
    INSERT INTO oldtbluser(id, user, password)
    VALUE (OLD.id, OLD.user, OLD.password);
END $$
DELIMITER ;



