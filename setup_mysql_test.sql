-- Prepare a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test' @'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';
