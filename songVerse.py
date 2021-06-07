
# Setting the initail variables
counter = 1
programStop = 1
verse = ""
fullVerse = ""
userInput = ""

# While loop that adds however many lines you want
while programStop == 1:
    
    # Gets lines to adds and stores them in a variable
    verse = input("Enter Verse ")
    strCounter = str(counter)
    counter = counter + 1
    fullVerse = fullVerse + " Line " + strCounter +": " + verse + "\n"
    userInput = input("Do you have another verse?")
   
   # IF loop to determine if you want to add more lines or print the song
    if userInput == "yes" or userInput == "Yes"  or userInput == "YES" or userInput == " yes" or userInput == " Yes" or userInput == " YES":
        programStop = 1 
    else:
        programStop = 0
        print(fullVerse)
    
    