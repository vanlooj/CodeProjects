import fileExtensionFunction

#Function to get a list put it in a dictionary and count the number of extensions based on type
def countExtension(listParm):

    #Creates the dictionary
    dictObject = dict()
    
    #Uses a for loop to go through the list
    for item in listParm:
        
        #Gets the type of estension by calling another function
        Extensions = fileExtensionFunction.parseExtension(item)
        
        #Either increase the account of the extension or adds it to the dictionary
        if (Extensions in dictObject.keys()):
             dictObject[Extensions] +=1
        else:
            dictObject[Extensions] = 1
            
    #Sorts the dictionary alphabetically and prints it       
    for i in sorted (dictObject) : 
        print((i, dictObject[i]))
   
#Test list used to test my program        
countExtension(["java.exe","C++.exe","convert.py","JustinWord.doc","songVerse.py"])
