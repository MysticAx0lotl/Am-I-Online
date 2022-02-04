##--setupModules.py - installs and imports all required libraries--##
##Author - Techguy791/Zee/CZSuperboy (I have a lot of aliases lol)
##Date - 2/4/2022

#Installs wheel, scratchclient, and tkinter if importLibs throws an error
def getLibs():
    os.system('py3 -m pip install wheel')
    os.system('py3 -m pip install scratchclient')
    os.system('py3 -m pip install tk')
    
#Sets up the libraries required for this project  
def importLibs():
    try:
        #Libraries must be defined as global to be used in other functions
        global ScratchSession
        global tk
        global os
        
        #Attempt to import scratchclient, tkinter, and os
        from scratchclient import ScratchSession
        import tkinter as tk
        import os
        
    #If the libraries cannot be imported
    except ImportError:
        
        #Tell the user we're installing the libraries
        print("One or more libraries are not installed. Installing now...")
        getLibs() #Call getlibs to install the libraries to the machine
        importLibs() #Recursively call importLibs to retry importing libraries
        
#Sets up the Scratch Session and returns it to the function that called it
def setupSession(uName, password):
    try:
        importLibs() #Install and set up all required libraries
        session = ScratchSession(uName, password) #Attempt to open a Scratch session using the provided uName and password
        return session #Returns the opened session to the function that called it
    
    except:
        print("An unhandled exception occured") #If something goes wrong, notify the user
        return 0 #Return 0 to show that the function terminated unsuccessfully
    
    

    
