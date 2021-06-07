#http get a file and save in python string variable
#check http  code

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

 
res = urllib.request.urlopen("http://ec2-35-173-47-64.compute-1.amazonaws.com/www.ferris.edu/online/future-students/index.html")
print(type(res))
#convert the response object data into a BeautifulSoup object
soup = BeautifulSoup(res,"html.parser")
 
#Get list of links
tags = soup('a')
for tag in tags:
    #search for text in the tag
    if "nursing" in str(tag).lower():
        nursing = open("nursing.txt", "a")
        nursing.write(str(tag))
        nursing.close()
    else:
        links= open("ferrisLinks.txt", "a")
        links.write(str(tag))
        links.close()
    
    

tags = soup('img')
for tag in tags:
    if "nursing" in str(tag).lower():
        nursing = open("nursing.txt", "a")
        nursing.write(str(tag))
        nursing.close()
    else:
        im = open("ferrisImages.txt", "a")
        im.write(str(tag))
        im.close()
        