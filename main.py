import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host="localhost",
    password="Wael#01007",
    user="root",
)


try:
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("create database if not exists schooldb")
        mycursor.execute("use schooldb")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if mydb.is_connected():
        print("MySQL connection is connected")
        
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS students(id int NOT NULL AUTO_INCREMENT, firstName varchar(50) NOT NULL, lastName varchar(50) NOT NULL, age int DEFAULT NULL, parentID int DEFAULT NULL, PRIMARY KEY(id), UNIQUE KEY UC_Names(firstName, lastName), CONSTRAINT CHK_PersonAge CHECK(age >= 16))"
        )
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS parents(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, firstName varchar(50) NOT NULL, lastName varchar(50) NOT NULL, age int DEFAULT NULL, address varchar(255) not null )"
        )

        mycursor.execute(
            "ALTER TABLE students  ADD  FOREIGN KEY (parentID) REFERENCES parents(id)"
        )

        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS fingerprint(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, finger varchar(255) NOT NULL, parentID int NOT NULL UNIQUE, foreign key (parentID) references parents(id) )"
        )
        mycursor.execute(
            "CREATE TABLE  IF NOT EXISTS subjects(id int NOT NULL AUTO_INCREMENT primary key, name varchar(80) NOT NULL)"
        )
        mycursor.execute(
            "CREATE TABLE  IF NOT EXISTS st_sub_piovt(id int NOT NULL AUTO_INCREMENT primary key,st_id int unique, sub_id int unique, foreign key (st_id) references students(id),foreign key (sub_id) references subjects(id))"
        )

    mycursor.close()
    mydb.close()
    print("MySQL connection is closed")
