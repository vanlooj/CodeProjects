import courseDictionary

ISINTuple = ("312","300","305")
ISYSTuple = ("371","200","288")
myDict = dict()
myDict["ISIN"] = courseDictionary.courseISIN(ISINTuple)
myDict["ISYS"] = courseDictionary.courseISYS(ISYSTuple)
print(myDict)

