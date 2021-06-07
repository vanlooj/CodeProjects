

# Function Determining an extensions type.
def parseExtension(fileName):
    return fileName[fileName.find('.') + 1 : len(fileName)]
    
  