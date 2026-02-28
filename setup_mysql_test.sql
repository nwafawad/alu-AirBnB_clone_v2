-- Task: Prepare the MySQL server for the AirBnB clone v2 test environment

-- Create the test database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the test user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to the test user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges on performance_schema to the test user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Apply all privilege changes
FLUSH PRIVILEGES;
