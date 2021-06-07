
# This function looks through the text file and determines the node that has the most failed user payments
def failedpayments(applog):
    
    #Variables for counting
    node2counter = 0
    node1counter = 0
    node3counter = 0
    node4counter = 0
    node5counter = 0
    node6counter = 0
    node7counter = 0
    
    #For loop to look through the file and if statements to see if the node failed a payment
    for line in applog:
        if "[node2]" in line:
            if "User Failed Payment" in line:
                node2counter += 1
        elif "[node1]" in line:
            if "User Failed Payment" in line:
                node1counter +=1
        elif "[node3]" in line:
            if "User Failed Payment" in line:
                node3counter +=1
        elif "[node4]" in line:
            if "User Failed Payment" in line:
                node4counter +=1
        elif "[node5]" in line:
            if "User Failed Payment" in line:
                node5counter +=1
        elif "[node6]" in line:
            if "User Failed Payment" in line:
                node6counter +=1
        elif "[node7]" in line:
            if "User Failed Payment" in line:
                node7counter +=1
    
    #See which node has the most user failed payments and display that to the screen
    if node1counter > node2counter and node1counter > node3counter and node1counter > node4counter and node1counter > node5counter and node1counter > node6counter and node1counter > node7counter:    
        return print("node1 has the most user failed payments " + str(node1counter)) 
    elif node2counter > node1counter and node2counter > node3counter and node2counter > node4counter and node2counter > node5counter and node2counter > node6counter and node2counter > node7counter:    
        return print("node2 has the most user failed payments " + str(node2counter))   
    elif node3counter > node2counter and node3counter > node1counter and node3counter > node4counter and node3counter > node5counter and node3counter > node6counter and node3counter > node7counter:    
        return print("node3 has the most user failed payments " + str(node3counter))
    elif node4counter > node2counter and node4counter > node3counter and node4counter > node1counter and node4counter > node5counter and node4counter > node6counter and node4counter > node7counter:    
         return print("node4 has the most user failed payments " + str(node4counter))
    elif node5counter > node2counter and node5counter > node3counter and node5counter > node4counter and node5counter > node1counter and node5counter > node6counter and node5counter > node7counter:    
        return print("node5 has the most user failed payments " + str(node5counter))
    elif node6counter > node2counter and node6counter > node3counter and node6counter > node4counter and node6counter > node5counter and node6counter > node1counter and node6counter > node7counter:    
        return print("node6 has the most user failed payments " + str(node6counter))
    elif node7counter > node2counter and node7counter > node3counter and node7counter > node4counter and node7counter > node5counter and node7counter > node6counter and node7counter > node1counter:    
        return print("node7 has the most user failed payments " + str(node7counter))            


# Function that gets the number of events that each node has and prints to the screen
def nodeevents(applog):
    
    #counter variables
    counter = 1
    counter1 = 1
    counter2 = 1
    counter3 = 1
    counter4 = 1
    counter5 = 1
    counter6 = 1
    counter7 = 1
    d = {}
    
    #For loop to look through the file and get the nodes and make those into a dictionary key. 
    #Also counts the number of events with if-else statements
    for line in applog:
        (key, val, val2) = line.split("-")
        if key in d:
            if "node1" in key:
                counter1 += 1
                d[key] = counter1  
            elif "node2" in key:
                counter2 += 1
                d[key] = counter2   
            elif "node3" in key:
                counter3 += 1
                d[key] = counter3  
            elif "node4" in key:
                counter4 += 1
                d[key] = counter4
            elif "node5" in key:
                counter5 += 1
                d[key] = counter5   
            elif "node6" in key:
                counter6 += 1
                d[key] = counter6   
            elif "node7" in key:
                counter7 += 1
                d[key] = counter7
        else:
            d[key] = counter
    
    #Print the dictionary to the screen
    return print(d)
  
       
#Function to look through the text file and gather the IPaddresses and create a unique list of them       
def IPaddress(applog):
    
    #For loop to go through all the ip addresses and then an if statement to see if they are already in the list. If not add them to it.
    IPlist = []
    for line in applog:
        (key, val, val2) = line.split("-")
        if val not in IPlist:
            IPlist.append(val)
    return IPlist
    
    
#Looks through the file and grabs out the event messages. Then creates a list of unique event messages    
def eventmessage(applog):
    messagelist = []
    
    #For loop to look through the file and an if statement to see if the message has been put into the list yet
    for line in applog:
        line = line.rstrip()
        (key, val, val2) = line.split("-")
        if val2 not in messagelist:
            messagelist.append(val2)
    return messagelist
   