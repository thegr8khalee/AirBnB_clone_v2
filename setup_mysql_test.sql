<<<<<<< HEAD
-- prepares a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @'localhost';
GRANT SELECT ON performance_schema.* To 'hbnb_test' @'localhost';
=======
-- Prepare a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';
>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3
