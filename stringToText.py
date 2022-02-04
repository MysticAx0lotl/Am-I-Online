##--stringToText.py - a port of the number to letter decoder used at https://scratch.mit.edu/projects/600796130/ --##
##Author - Techguy791/Zee/CZSuperboy (I have a lot of aliases lol)
##Date - 2/4/2022

#Dictionary that corressponds every supported letter to a number
numLetters = dict([ ('91', 'A'),
                    ('92', 'B'),
                    ('93', 'C'),
                    ('94', 'D'),
                    ('95', 'E'),
                    ('96', 'F'),
                    ('97', 'G'),
                    ('98', 'H'),
                    ('99', 'I'),
                    ('10', 'J'),
                    ('11', 'K'),
                    ('12', 'L'),
                    ('13', 'M'),
                    ('14', 'N'),
                    ('15', 'O'),
                    ('16', 'P'),
                    ('17', 'Q'),
                    ('18', 'R'),
                    ('19', 'S'),
                    ('20', 'T'),
                    ('21', 'U'),
                    ('22', 'V'),
                    ('23', 'W'),
                    ('24', 'X'),
                    ('25', 'Y'),
                    ('26', 'Z'),
                    ('53', '/'),
                    ('54', '-'),
                    ('55', '_')])

#Convert a string of numbers to a string of letters
def convertToString(string):

    #Initialize variables
    finalString = ""
    index = 0;

    #While the index is in bounds
    while index <= (len(string) - 1):
        letter = ""

        #Get the next 2 characters
        for j in range(2):
            letter += string[index]
            if index <= (len(string) - 1):
                index += 1
                
        #Find the corresponding letters from the dictionary
        finalString += numLetters[letter]

    #Return the string
    return finalString
    
