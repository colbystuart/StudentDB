#Connecting to Database "Students"

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

#mycursor.execute("ALTER TABLE Students ADD COLUMN phoneNumber VARCHAR(15);")

#mycursor.execute("DESCRIBE Students")

#for x in mycursor:
#    print(x)
