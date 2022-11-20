CREATE DATABASE movies_controll;
CREATE TABLE MOVIES (
id INT PRIMARY KEY auto_increment,
tipo CHAR (1) NOT NULL,
nome VARCHAR (30) NOT NULL,
total_ep INT,
atual_ep INT,
last_view DATE DEFAULT CURRENT_TIMESTAMP() 
); 






