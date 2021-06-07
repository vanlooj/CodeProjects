import fileExtensionFunction

#Function that looks through files for extension of your choice
def fileExtensionExist(fileList, fileExtension):
    
    # For loop to look through the lists of files
    for fileName in fileList:
        listEnd = fileList[-1]
        extension = fileExtensionFunction.parseExtension(fileName)
        
        # Checks if extension matches the on you wants
        if extension == fileExtension:
            return True
        else:
            
            # Checks if you have looked through all the files. If so returns false
            if fileName == listEnd:
                return False
                
# Inputs a list of files to look through          
print(fileExtensionExist(["java.exe","C++.exe","convert.py","JustinWord.doc","Notes.txt"],".doc"))
        
            
        