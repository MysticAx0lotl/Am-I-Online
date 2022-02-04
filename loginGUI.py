##--GUI.py - handles the GUI of the login screen--##
##Author - Techguy791/Zee/CZSuperboy (I have a lot of aliases lol)
##Date - 2/4/2022

#Import all required libs from Tkinter
from tkinter import *
from tkinter import ttk

#Setup the window
window = Tk()
frm = ttk.Frame(window, padding=15)
frm.grid()

#
def submitData():
    global credentials
    credentials = []
    credentials.append(uNameEntry.get())
    credentials.append(passEntry.get())
    credentials.append(iEntry.get())
    window.destroy()

def loginPrompt():
    global uNameEntry, passEntry, iEntry
    uLabel = ttk.Label(frm, text="Scratch Username:")
    uNameEntry = ttk.Entry(frm)
    pLabel = ttk.Label(frm, text="Scratch Password:")
    passEntry = ttk.Entry(frm, show = '*')
    idLabel = ttk.Label(frm, text="ID of your \"Am I Online?\" remix")
    iEntry = ttk.Entry(frm)
    button = ttk.Button(frm, text="Submit", command=submitData)

    uLabel.pack()
    uNameEntry.pack()
    pLabel.pack()
    passEntry.pack()
    idLabel.pack()
    iEntry.pack()
    button.pack()

    window.mainloop()

    return credentials

    
