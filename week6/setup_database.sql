# create_databases.sql

#     Most Linux distributions include the MariaDB client instead of the Oracle MySQL client. To install the MySQL command-line client on Amazon Linux 2023, run the following command:
#
#
# sudo dnf install mariadb105
# To install the MySQL command-line client on Amazon Linux 2, run the following command:
#
#
# sudo yum install mariadb
# To install the MySQL command-line client on most DEB-based Linux distributions, run the following command:
#
#
# apt-get install mariadb-client
# To check the version of your MySQL command-line client, run the following command:
#
#
# mysql --version

# mysql -h db.cd02ia4k8ew2.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
# source sql.txt


/***********************************************************
* Create the database named demo, its tables, and a user
************************************************************/

DROP DATABASE IF EXISTS demo;

CREATE DATABASE demo;

USE demo;

CREATE TABLE User
(
    UserID    INT NOT NULL AUTO_INCREMENT,
    Email     VARCHAR(50),
    FirstName VARCHAR(50),
    LastName  VARCHAR(50),

    PRIMARY KEY (UserID)
);

INSERT INTO User
    (Email, FirstName, LastName)
VALUES ('jsmith@gmail.com', 'John', 'Smith'),
       ('andi@demo.com', 'Andrea', 'Steelman'),
       ('joeldemo@yahoo.com', 'Joel', 'demo');
