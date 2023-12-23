-- Prepares MySQL server for the project
-- creates a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates a user for the database and sets a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all privileges on db to the user
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT on perfomance_schema.* TO 'hbnb_dev'@'localhost';
