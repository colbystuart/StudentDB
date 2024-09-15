#including dbconnect function to use in this file
from dbconnect import db_connect

#declaring cursor to database
db = db_connect()
mycursor = db.cursor()

#helper function to make sure a student exists or if the user typed the name in wrong
def student_exists(first_name, last_name):
    mycursor.execute("SELECT EXISTS(SELECT 1 FROM Students WHERE first_name = %s and last_name = %s)", (first_name, last_name))
    return bool(mycursor.fetchone()[0])

def add_student():
    
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    grade = input("Enter Grade Level: ")
    gpa = input("Enter GPA: ")
    email = input("Enter Email: ")
    phoneNumber = input("Enter Phone Number: ")

    mycursor.execute("INSERT INTO Students (first_name, last_name, grade, gpa, email, phoneNumber) VALUES (%s, %s, %s, %s, %s, %s)", (firstName, lastName, grade, gpa, email, phoneNumber))
    db.commit()

    print("\nStudent Added.\n")

def delete_student():

    print("Please input the first name of the student to be deleted: ")
    first_name = input()
    print("Please input the last name of the student to be deleted: ")
    last_name = input()

    if student_exists(first_name, last_name):
        mycursor.execute("DELETE FROM Students WHERE first_name = %s AND last_name = %s", (first_name, last_name))
        db.commit()
        print("\nStudent Deleted.\n")
    else:
        print("Student Not Found.\n")
    

def edit_student():
    first_name = input("What is the first name of the student you wish to edit?\n")
    last_name = input("Last name?\n")
    if (student_exists(first_name, last_name)):
        to_edit = input("\nWould you like to edit: First Name, Last Name, Grade, GPA, Email, or Phone Number?\n")
        if (to_edit.lower() == "first name"):
            new_first_name = input("\nWhat would you like to change their first name to?\n")
            mycursor.execute("UPDATE Students SET first_name = %s WHERE first_name = %s AND last_name = %s", (new_first_name, first_name, last_name))
            db.commit()
            print("Student's name edited successfully")
        elif (to_edit.lower() == "last name"):
            new_last_name = input("\nWhat would you like to change their last name to?\n")
            mycursor.execute("UPDATE Students SET last_name = %s WHERE first_name = %s AND last_name = %s", (new_last_name, first_name, last_name))
            db.commit()
            print("Student's name edited successfully")
        elif (to_edit.lower() == "grade"):
            new_grade = input("What would you like to change their grade to: \n")
            mycursor.execute("UPDATE Students SET grade = %s WHERE first_name = %s AND last_name = %s", (new_grade, first_name, last_name))
            print("Student's grade was changed successfully")
            db.commit()
        elif (to_edit.lower() == "gpa"):
            new_gpa = input("What would you like to change their GPA to: \n")
            mycursor.execute("UPDATE Students SET gpa = %s WHERE first_name = %s AND last_name = %s", (new_gpa, first_name, last_name))
            db.commit()
        elif (to_edit.lower() == "email"):
            new_email = input("What would you like to change their email to: \n")
            mycursor.execute("UPDATE Students SET email = %s WHERE first_name = %s AND last_name = %s", (new_email, first_name, last_name))
            db.commit()
        elif (to_edit.lower() == "phone number"):
            new_phone_number = input("What would you like to change their phone number to: \n")
            mycursor.execute("UPDATE Students SET phoneNumber = %s WHERE first_name = %s AND last_name = %s", (new_phone_number, first_name, last_name))
            db.commit()
        else:
            print("Invalid Entry\n")
    else:
        print("Invalid Name")
        


def view_table():       
    mycursor.execute("SELECT * FROM Students")

    for x in mycursor:
        print(x)


def main():
    while True:
        option = input("\nWould you like to: \n[0] Exit \n[1] Add A Student \n[2] Delete a Student \n[3] Edit a Student's Details \n[4] View Table \n\n")

        if option == '0':
            print("Exiting")
            break
        elif option == '1':
            add_student()
        elif option == '2':
            delete_student()
        elif option == '3':
            edit_student()
        elif option == '4':
            view_table()
        else:
            print("Invalid option. Please enter a number 0-6.\n")

if __name__  == '__main__':
    main()