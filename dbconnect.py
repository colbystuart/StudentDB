#Connecting to Database "Students"

#To initialize the database 
#remove the database variable from db_connect

import mysql.connector

def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Students"
    )
db = db_connect()
mycursor = db.cursor()

#Use this command to create the database
#mycursor.execute("CREATE DATABASE IF NOT EXISTS Students")
#add  database="Students"  back to db_connect

#Use this command to create the table
#mycursor.execute("""
#    CREATE TABLE IF NOT EXISTS students_info (
#        first_name VARCHAR(255),
#        last_name VARCHAR(255),
#        grade INT,
#        id INT AUTO_INCREMENT PRIMARY KEY,
#        gpa FLOAT,
#        email VARCHAR(255),
#        phoneNumber VARCHAR(15)
#    )
#""")