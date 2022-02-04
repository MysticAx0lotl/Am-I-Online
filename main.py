##--main.py - the main executable, this is where the magic happens--##
##Author - Techguy791/Zee/CZSuperboy (I have a lot of aliases lol)
##Date - 2/4/2022

#Import all required python scripts
from setupModules import setupSession
from stringToText import convertToString
import fileManager

#Open and start a Scratch session
def startSession(username, password):

    #Call setupSession from setupModules
    session = setupSession(username, password)

    #If setupSession was successful
    if session != 0:
        print("Login Success!")
        return session

    #If it was unsuccessful
    elif session == 0:
        print("Login Failed")
        return 0

#Open a hook onto the specified project ID 
def hookProject(session, identifier):
    cloud = session.create_cloud_connection(identifier)
    print("Connected to scratch.mit.edu/projects/" + identifier)
    return cloud

#Make sure the user trying to access the project is allowed to do so
def authenticateUser(username, allowedUser):
    print(username)
    print(allowedUser)
    #If the key fits the lock
    if username == allowedUser:

        #Return True
        print("Authenticated!")
        return True
    else:
        
        #Return False
        print("Project Authentication Failed")
        return False

#Main function
def main():
    data = fileManager.openData() #Get username, password, and project ID
    session = startSession(data[0], data[1]) #Open a Scratch session

    #If all was successful
    if session != 0:
        project = hookProject(session, data[2]) #Open a hook on the desired project
        
    #Get the encoded username from the Scratch project's "allowedUser" variable and convert to a useable string
    allowedName = convertToString(project.get_cloud_variable("allowedUser"))

    #Pass the lock (allowedName) and the key (the provided username) to authenticateUser
    unlocked = authenticateUser(data[0].upper(), allowedName)

    #Here's where the fun begins...
    if unlocked:
        #importing onlinePrompt is conditional as the script triggers as soon as it's loaded
        from mainGUI import onlinePrompt
        onlinePrompt(project)
        
#Run main() if __name__ matches __main__       
if __name__ == "__main__":
    main()
