# The code in this file contains:
# Function for the register service
# Function to display service to user
# 

#import service dictionary
import records
import helperFunctions
import providerDirectory
from dataRepository import DataRepository
from datetime import datetime
from colorama import Fore
from colorama import Style

def registerService(dataRepository : DataRepository): #register data and time of service and store into records
    serviceNumber
    while True:
        serviceNumber = helperFunctions.informationPrompter("Enter service code", 1, 9)
        if displayService(serviceNumber) == True:
            break
    memberNumber = helperFunctions.informationPrompter("Enter member number", 1, 9)
    providerNumber = helperFunctions.informationPrompter("Enter Provider number", 1, 9)
    currentTime = datetime.now()
    serviceDate = currentTime.strftime("%m/%d/%Y %H:%M:%S") #UTC time
    comments = helperFunctions.informationPrompter("Enter a comment", 0, 100)
    records.addRecord(serviceDate, providerNumber, memberNumber, serviceNumber, comments)
    return True

# code to check service code is correct
    # return true if service matches what the user wants 
    # return false WITH error code if input doesnt match a service 
    # return false if input doesnt match a service
def displayService(userInput: str):
    # Initialize provider directory data
    providerDir = providerDirectory.Directory()
    providerDir.read()
    # get userInput from service dictionary
    # The dictionary consists of [service # : service information]
    service = providerDir.dictionary.get(userInput,0)
    # check to see if userInput is in the dictionary 
    if service == 0:
        # Error message and return false
        print(f'{Fore.RED}ERROR:{Style.RESET_ALL} No servivce corresponds to service number entered')
        return False
    # display service and ask user if it is correct
    print (service[0])
    user = input("Is this the correct service (y/n): ")
    # make sure user inputs y/Y or n/N
    while user not in ['y', 'Y', 'n', 'N']:
        user = input("Is this the correct service (y/n): ")
    if user in ['n', 'N']:
        # service number is wrong and it returns False
        return False
    # service number is correct and it returns True
    return True

