from dataRepository import DataRepository
import helperFunctions

def interactiveMode(dataRepository : DataRepository):
    choice = -1
    menuOptions = \
        ["Add a member.",\
        "Remove a member.",\
        "Modify a member's information.",\
        "Add a provider.",\
        "Remove a provider.",\
        "Modify a provider's information.",\
        "Return to previous menu."]
    endOption = len(menuOptions)
    while choice != endOption:
        print("What would you like to do?")
        choice = helperFunctions.menuManager(menuOptions)
        if choice == 1:
            insertMember(dataRepository)
        elif choice == 2:
            removeMember(dataRepository)
        elif choice == 3:
            modifyMember(dataRepository)
        elif choice == 4:
            insertProvider(dataRepository)
        elif choice == 5:
            removeProvider(dataRepository)
        elif choice == 6:
            modifyProvider(dataRepository)
    return

def insertMember(dataRepository : DataRepository):
    dataRepository.insertMember()

def removeMember(dataRepository : DataRepository):
    number = None
    validNumber = False
    while validNumber == False:
        number = input("What is the 9-digit number of the member you would like to remove?: ")
        validNumber = helperFunctions.validNumberCheck(number)
        if validNumber == False:
            print("Invalid number.")
    number = int(number)
    memberRemoved = dataRepository.removeMember(number)
    if memberRemoved:
        print("Member removed.")
    else:
        print("Member does not exist.")

def modifyMember(dataRepository : DataRepository):
    validNumber = False
    while validNumber == False:
        number = input("What is the 9-digit number of the member you would like to remove?: ")
        validNumber = helperFunctions.validNumberCheck(number)
        if validNumber == False:
            print("Invalid number.")
    number = int(number)
    member = dataRepository.retrieveMember(number)
    if member == None:
        print("Member does not exist.")
    else:
        member.adjustMember()

def insertProvider(dataRepository : DataRepository):
    pass

def removeProvider(dataRepository : DataRepository):
    pass

def modifyProvider(dataRepository : DataRepository):
    pass