# Am I Online
A way to tell your followers on Scratch whether or not you're online

#Important: This is **not functional** just yet.

**Setup Instructions:**

 1. Make a remix of [this Scratch project](https://scratch.mit.edu/projects/639147574/) and jot down the project ID
 2. **Create an alternate/dummy account**. Due to what's presumably a quirk with the Scratch API, you **cannot** use the same account you remixed the project with  to interface with the cloud variables
 3. Encode your username by clicking the "encode username" block in your remix
 4. Download all the code in this repo
 5. [Install Python ](https://www.python.org/). For some strange reason, executables generated with auto-py-to-exe report false positives with virus scanners.
 6. Double-click the "main" file to start the program
 7. Login with your alternate account's username and password, and paste the ID (**not the whole link**) of your remixed project. This code **does** save your username and password to a .dat file for future reference. It **is not capable** of sending the information within the .dat file **anywhere except for the Scratch servers**
 8.  You're all set up! A window will now appear that will give you the option to toggle wether you're appearing online or offline. Click that twice and the program will begin to function. Clicking the button after that will update your status in real time. After exiting the program, your status will be saved to the Scratch project. Simply run main.py again if you want to change your status again.

If you have any questions or issues, please feel free to submit an issue, or contact me on my [scratch profile](https://scratch.mit.edu/users/CZSuperboy/). Enjoy!

~Zee
