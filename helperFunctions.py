#This holds any helper functions that may be useful
#accross multiple files

#This function takes a string and length bounds, and returns 0 if the
#string is within the bounds, 1 if is outside the maximum bound,
#and -1 if it is below the minimum bound.
def stringLengthCheck(string : str, minLength : int, maxLength : int) -> int:
    stringLength = len(string)
    if stringLength < minLength:
        return -1
    if stringLength > maxLength:
        return 1
    return 0

#Prompts user for information about a specific subject. 
#For example "What is the member name (1 character(s) minimum, 25 character(s) maximum.
#Also handles length checking.
#Returns the final input string to the user.
def informationPrompter(promptTarget : str, minLength : int, maxLength : int) -> str:
    correctString = False
    string = None
    while correctString == False:
        print("What is the " + promptTarget + " (" + str(minLength) + " character(s) minimum, "\
              + str(maxLength) + " character(s) maximum)?")
        string = input()
        stringValidity = stringLengthCheck(string, minLength, maxLength)
        if stringValidity == 0:
            correctString = True
        elif stringValidity == -1:
            print("Your input is below the minimum accepted length. Please input again.")
        elif stringValidity == 1:
            print("Your input is above the maximum accepted length. Please input again.")
    return string

#Prompts for yes/no, and returns true for yes and false for no.
def yesNoPrompter() -> bool:
    validInput = False
    response = None
    while validInput == False:
        yesNo = input("Enter Y/N: ")
        yesNoValue = yesNoChecker(yesNo)
        if yesNoValue == 1:
            response = True
            validInput = True
        elif yesNoValue == -1:
            response = False
            validInput = True
        else:
            print("Invalid input.")
    return response

#turns yes/no statements into other values. 1 == yes, -1 == no, 0 == invalid input.
def yesNoChecker(yesNo : str) -> int:
    if yesNo == "Y" or yesNo == "y" or yesNo == "Yes" or yesNo == "yes":
        return 1
    if yesNo == "N" or yesNo == "n" or yesNo == "No" or yesNo == "no":
        return -1
    return 0