##--mainGUI.py - the GUI that handles toggling online and offline appearance--##
##Author - Techguy791/Zee/CZSuperboy (I have a lot of aliases lol)
##Date - 2/4/2022

#Import everything required from Tkinter
from tkinter import *
from tkinter import ttk

#Setup window
window = Tk()
frm = ttk.Frame(window, padding=25)
frm.grid()

#This literally just closes the program
def exitProgram():
    window.destroy()

#This toggles the value of the "isOnline" variable in the Scratch project
def updateOnlineStatus():
    
    onlineStatus = cloudConnection.get_cloud_variable("isOnline") #Get current state of isOnline and save it to an integer
    setStatus = 0 #This variable will be what's sent to the project

    if onlineStatus == 1: #If you're currently appearing online
        setStatus = 0 #Appear offline (represented by 0)
        statusLabel.config(text="You are currently appearing offline") #Change the label of the statusLabel object

    elif onlineStatus == 0:
        setStatus = 1 #If you're currently appearing offline
        statusLabel.config(text="You are currently appearing online") #Change the label of the statusLabel object

    #print(onlineStatus) #Debugging feature to make sure this function is working properly
    cloudConnection.set_cloud_variable("isOnline", setStatus) #Write setStatus to the Scratch project's isOnline variable

#The primary function of this library, starts and manages the GUI
def onlinePrompt(cloud):
    
    global statusLabel, cloudConnection #These need to be global to be able to be modified by updateOnlineStatus
    cloudConnection = cloud #This makes managing the cloud connection possible, as you can't set an argument to be global AFAIK
    status = cloudConnection.get_cloud_variable("isOnline")

    #Set up all GUI widgets
    statusLabel = ttk.Label(frm, text="Ready to go!")
    button = ttk.Button(frm, text="Toggle Online/Offline", command=updateOnlineStatus)#For some reason you have to click the button twice for updateOnlineStatus to actually function, if anyone knows how to fix this, please submit a PR
    exitButton = ttk.Button(frm, text="Exit", command=exitProgram) #This button will exit the program

    #Pack all widgets
    statusLabel.pack()
    button.pack()
    exitButton.pack()

    #Main loop for the window
    window.mainloop()
