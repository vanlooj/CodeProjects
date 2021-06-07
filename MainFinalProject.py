import FinalProject
import sqlite3

CONNECTION = sqlite3.connect('finaldata.sqlite3')

#instantia a cursor object
cursor = CONNECTION.cursor()

#create tables
cursor.execute('DROP TABLE IF EXISTS IPAddress')
cursor.execute('CREATE TABLE IPAddress (id INTEGER PRIMARY KEY AUTOINCREMENT, IPAddressText VARCHAR(25))')
cursor.execute('DROP TABLE IF EXISTS EventMessage')
cursor.execute('CREATE TABLE EventMessage (id INTEGER PRIMARY KEY AUTOINCREMENT, messageText VARCHAR(50))')
exit = ""

#While loop to ask user for input on what they want to do
while exit != "exit":
    print("==========================================================")
    print("Enter 1 to see which node has the most failed payments" +'\n'+
    "Enter 2 to see the number of events each node has"+'\n'+
    "Enter 3 to see a list of unique IP Addresses"+'\n'+
    "Enter 4 to see a list of unique event messages"+'\n'+
    "Enter 5 to save the list of IP addresses to a database"+'\n'+
    "Enter 6 to save the event messages to a database"+'\n'+
    "Enter exit to quit")
    print("===========================================================")
    userInput = input("Enter number here ")
    
    #If-elif statements to run the users commands
    # Runs the function failedpayments
    if userInput == "1":
        with open("Applog.txt") as applog:
            readApp = FinalProject.failedpayments(applog)
    
    #Runs the function nodeevents
    elif userInput == "2":
        with open("Applog.txt") as applog:
            readApp = FinalProject.nodeevents(applog)
    
    #Runs the function IPaddress
    elif userInput == "3":
        with open("Applog.txt") as applog:
            readApp = FinalProject.IPaddress(applog)
        print(readApp)
        
    #Runs the function eventmessage
    elif userInput == "4":
        with open("Applog.txt") as applog:
            readApp = FinalProject.eventmessage(applog)
        print(readApp)
    
    #Writes the output of the IP addresses to a database
    elif userInput == "5":
        with open("Applog.txt") as applog:
            addressIP = FinalProject.IPaddress(applog)
            lenadd = len(addressIP)
            count = 0
        for line in addressIP:
            if lenadd > count:
                cursor = CONNECTION.cursor ()
                cursor.executemany('INSERT INTO IPAddress (IPAddressText) VALUES (?)', (line))
                CONNECTION.commit()
                cursor.close()
                count += 1
        print("Successful")
        
    #Writes teh event messages to a database
    elif userInput == "6":
        with open("Applog.txt") as applog:
            messagesEvent = FinalProject.eventmessage(applog)
            lenadd = len(messagesEvent)
            count = 0
        for line in messagesEvent:
            if lenadd > count:
                cursor = CONNECTION.cursor ()
                cursor.executemany('INSERT INTO EventMessage (messageText) VALUES (?)', (line))
                CONNECTION.commit()
                cursor.close()
                count += 1
        print("Successful")
    
    #Exits the program
    elif userInput == "7":
        exit = "exit"
    
