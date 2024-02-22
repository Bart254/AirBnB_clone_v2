-- Prepares MySQL server for the project
-- creates a database hbnb_test
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creates hbnb_test user with password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
-- Sets privileges for hbnb_test user
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
