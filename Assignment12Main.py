import sqlite3
import hashlib

#create database
conn = sqlite3.connect('userdb.sqlite3')

#instantia a cursor object
cur = conn.cursor()

#create table
cur.execute('DROP TABLE IF EXISTS Users')
cur.execute('CREATE TABLE Users(username TEXT, password TEXT)')

cur = conn.cursor()

#create a user record with unhashed password of "WeakPassword"
cur.execute('INSERT INTO Users (username, password) VALUES (?,?)', ('student1','460899c942673a93b86a81ca6297cd36'))

conn.commit()


while 1==1:

    #TO DO #1 prompt use the user for a user name and password.  
    #store the entered username in a varaible named "uname"
    #store the entered password in a varaible named "pswd"
    uname = input("Enter your user name")
    pswd = input("Enter your password")

    #TO DO #2 hash the user provided password (pswd) as an md5 hash using hashlib and store in variable name pswdHash
    hash_object = hashlib.md5(pswd.encode())
    pswdHash = hash_object.hexdigest()
    
    #fetch the hashed password from the database for the user uname (the followin code is vulnerble to SQL Injection...)
    cur.execute("SELECT password from Users WHERE username = '" + uname + "'")
    row=cur.fetchone()
    
    if row == None:
        print ("user name is incorrect.  Try again...")
  
    else:
        #TO DO #3.  row variable is a tuple.   Compare the first element in the row tuple to your hashed password pswdHash
        #display appropriate messages to user.   "break" if the hashed password are equal
        if pswdHash == row[0]:
            print("The password is correct")
            break
        else:
            print("Incorrect Password")
            pswd = input("Try entering password again")
            hash_object = hashlib.md5(pswd.encode())
            pswdHash = hash_object.hexdigest()
            if pswdHash == row[0]:
                print("The password is correct")
                break
            else:
                print("invalid user name")
            
    

#close database connection
conn.close()