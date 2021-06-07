import hashlib
import os


#Looks at the files in my directory
for filename in os.listdir('.'):
    if not os.path.isdir(filename):
        
        #Opens the file and reads it.
        fileopened = open(filename, 'r', encoding = 'ISO-8859_1')
        fileread = fileopened.read()
        
        #Gets the hash of the content of the files
        fileHashed = hash(fileread)
        
        #Opens a file to write to and then writes the file name and hash to it
        filehash = open("filehashes.txt", 'a')
        filehash.write(filename + "\t" + str(fileHashed) + "\r")