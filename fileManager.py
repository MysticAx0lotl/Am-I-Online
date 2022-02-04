##--fileManager.py - this library handles the creation and processing of the file "isOnline.dat"--##
##Author - Techguy791/Zee/CZSuperboy (I have a lot of aliases lol)
##Date - 2/4/2022

from os.path import exists #Used for checking if "isOnline.dat" is present without any complex workarounds

#Loads the login GUI and saves its input to the specified file object
def getData(fileObject):
    import loginGUI #importing GUI is conditional as the script triggers as soon as it's loaded
    data = loginGUI.loginPrompt()
    for thing in data: #loginPrompt returns a list
        fileObject.write(thing) #Write each object of that list to the file object
        fileObject.write("\n") #Write a newline character to make retreiving the data easier

#Reads every line in a file object and returns the result as a list
def readFile(file):
    data = []
    for line in file:
        data.append(line) #Add each line of data from the file object to "data"
    return data 

#This function controls the opening of, reading from, and/or writing to of "isOnline.dat"
def openData():
    
    data = []
    
    if exists("isOnline.dat"): #If "isOnline.dat" exists in the working directory
        try:
            f = open('isOnline.dat', 'r') #Open "isOnline.dat" 
            data = readFile(f) #Call readFile and pass the file object
            f.close() #Close the file object
            
        except: #In the odd case that something goes wrong (e.g. "isOnline.dat" contains no data/too much data)
            print("Something went wrong. A crash is imminent") #Warn the user that the program isn't going to function properly anymore

    else: #If the system reports "isOnline.dat" does not exist
        try:
            f = open('isOnline.dat', 'a') #Create the file and open for writing
            getData(f) #Call getData and prompt the user for the required information
            f.close() #Close the file object before reopening it for writing
            f = open('isOnline.dat', 'r') #Open the newly-created file for writing
            data = readFile(f) #Call readFile and pass the file object
            f.close() #Close "isOnline.dat"
        except: #Second verse
            print("Something went wrong. A crash is imminent") #Same as the first

    results = [] #Create a blank list

    for line in data: #For each line in the data list (this is where the program will likely break if something went wrong handling the file)
        results.append(line.strip("\n ")) #Strip whitespaces and newline characters from each line

    return results #Returned the processed data
