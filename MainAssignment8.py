import Assignment8

# Opens file and passes it to our createRainbow function
englishFile = open("english.txt", "r", encoding = "ISO-8859_1")
rainbow = Assignment8.createRainbow(englishFile)
print("hash file created")
    
# Gets users password they want to validate
userPsswd = Assignment8.validatePassword(input("Input Password "))
