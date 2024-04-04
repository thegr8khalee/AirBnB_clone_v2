<<<<<<< HEAD
-- prepares a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';
=======
-- Prepare a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';
>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3
