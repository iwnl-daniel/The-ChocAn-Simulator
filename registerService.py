# The code in this file contains:
# Function for the register service
# Function to display service to user
# 

#import service dictionary

def registerService():
    while True:
        serviceNumber = input("Please enter the service number: ")
        if displayService(serviceNumber) == True:
            break
    # addRecord() when available
    return True

# code to check service code is correct
    # return true if service matches what the user wants 
    # return false WITH error code if input doesnt match a service 
    # return false if input doesnt match a service
def displayService(userInput: int):
    # get userInput from service dictionary
    # The dictionary consists of [service # : service information]
    service = NAME_OF_SERVICE_DIRECTORY.get(userInput,0)
    # check to see if userInput is in the dictionary 
    if service == 0:
        # Error message and return false
        print("\033[31mERROR:\x1b[0m No servivce corresponds to service number entered")
        return False
    # display service and ask user if it is correct
    print (service)
    user = input("Is this the correct service (y/n): ")
    # make sure user inputs y/Y or n/N
    while user not in ['y', 'Y', 'n', 'N']:
        user = input("Is this the correct service (y/n): ")
    if user in ['n', 'N']:
        # service number is wrong and it returns False
        return False
    # service number is correct and it returns True
    return True




    
