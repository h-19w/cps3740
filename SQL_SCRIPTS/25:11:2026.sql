CREATE DATABASE `CPS*3740`;

USE `CPS*3740`;


CREATE TABLE students (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    student_id VARCHAR(20) NOT NULL UNIQUE,
    gender VARCHAR(20),
    email VARCHAR(100),
    phone VARCHAR(20)
);

DESCRIBE students;

INSERT INTO students
(student_name, student_id, gender, email, phone)
VALUES
('John Tan', '12345', 'Male', 'john@email.com', '91234567');

SELECT * FROM students;
DESCRIBE students;