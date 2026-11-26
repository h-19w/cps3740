USE triggerdb;

/*
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employeeNUMBER INT NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    changedate DATETIME DEFAULT NULL, 
    action VARCHAR(50) DEFAULT NULL,
    salary INT NOT NULL
);

CREATE TABLE employees_audit(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    employeeNUMBER INT NOT NULL, 
    lastname VARCHAR(50) NOT NULL, 
    changedate DATETIME DEFAULT NULL, 
    action VARCHAR(50) DEFAULT NULL
);

CREATE TABLE employees_deleted (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    employeeNumber  INT          NOT NULL,
    lastname        VARCHAR(50)  NOT NULL,
    deleted_at      DATETIME     NOT NULL
);

*/

SELECT * FROM employees;
SELECT * FROM employees_audit;

SHOW TRIGGERS in triggerdb; -- SHOWS THE TRIGGERS IN THE DATABASE
/*
-- for updating
DELIMITER $$
CREATE TRIGGER before_employee_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employees_audit
    SET action = 'update',
        employeeNumber = OLD.employeeNumber,
        lastname = OLD.lastname,
        changedate = NOW();
END $$
DELIMITER ;
*/

DESCRIBE employees;
DESCRIBE employees_audit;
/*
-- condition for GUIDING the user -- if negative salary? 
DELIMITER $$
CREATE TRIGGER check_employee_salary
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = "Salary cannot be negative";
    END IF;
END $$
DELIMITER ;
*/

/*
-- for deleting 
DELIMITER $$
CREATE TRIGGER after_employee_delete
AFTER DELETE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employees_deleted
    (employeeNUMBER, lastname, deleted_at)
    VALUES (OLD.employeeNUMBER, OLD.lastname, NOW());
END $$
DELIMITER ;
*/


SELECT * FROM employees_deleted;
DESCRIBE employees_deleted;

SHOW TRIGGERS IN triggerdb;