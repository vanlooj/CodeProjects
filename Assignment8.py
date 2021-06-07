
# a function that writes a pasword as a hash to a file
def writeHashedPsswd():
    import hashlib
   
   #Trys to perform the following code
    try:
        
        #Gets usre input and hashes it
        userPassword = input("Input Password")
        userPassword = hashlib.md5('ISO-8859-1 encoding')
        
        #Writes the hash to a file
        psswdFile = open("filePsswd.txt", "w")
        psswdFile.write(userPassword+'\n')
        psswdFile.close()
        
    #Prints if there is an error in the above code
    except:
        print("An error occurred")
        
# function to right the hash of a file contents to another file       
def createRainbow(englishFile):
    
    #opens the file that we will write to
    fileEnglishRainbow = open("englishRainbow.txt", "a")
    
    # uses for loop to read through a file
    for line in englishFile:
       
        #Gets the hash for the current line of a file and turns it into a string
        hLine = hash(line)
        strLine = str(hLine)
        
        #Writes the hash to a file
        fileEnglishRainbow.write(strLine)
        fileEnglishRainbow.write("\n")
    fileEnglishRainbow.close()
    return fileEnglishRainbow
  
# A function to get a password and validate it  
def validatePassword(pwd):
   
    # declare some variables
    special =""
    number =""
    length =""
    upperCase =""
    
    # Gets the length of password and checks if its greater or equal to 8
    pwdLength = len(pwd)
    if pwdLength >=8:
        length = "True"
    else:
        return False
        
    #Goes through the characters of a password and see if they have a number or special character in it.
    for char in pwd:
        if char in '01234567890':
            number = "True"
        if char in '!@#$%^&*()=+':
            special = "True"
    
    # Checks to see if they have an uppercase in the password
    if any(char.isupper() for char in pwd):
        upperCase = "True"
        
    # If password meets the requirements print true. If not print fals.
    if length == "True" and number == "True" and special == "True" and upperCase == "True":
        return print(True)
    else:
        return print(False)
    