import helperFunctions
from dataRepository import DataRepository
import interactiveMode

#This file will be where the program is run from, and it
#will be in charge of controlling the flow of the program.

def main():
    dataRepository = DataRepository()
    choice = -1
    menuOptions = \
        ["Member Mode",\
        "Provider Mode",\
        "ChocAn Mode",\
        "Close Program"]
    endOption = len(menuOptions)
    while choice != endOption:
        print("What user mode would you like to use?")
        choice = helperFunctions.menuManager(menuOptions)
        if choice == 1:
            memberMenu(dataRepository)
        elif choice == 2:
            providerMenu(dataRepository)
        elif choice == 3:
            chocAnMenu(dataRepository)
    return

def memberMenu(dataRepository : DataRepository):
    choice = -1
    menuOptions = \
        ["Member Login", \
         "Return to user mode selection."]
    endOption = len(menuOptions)
    while choice != endOption:
        print("Please select an option.")
        choice = helperFunctions.menuManager(menuOptions)
        if choice == 1:
            print("Please enter your Member ID:")
            number = input()
            member = dataRepository.validateMember(number)
            if member is not None:
                print("\nWelcome,", member.memberName)
                terminal = input()  # used to pause program at this point
        elif choice == 2:
            pass
    return

def providerMenu(dataRepository : DataRepository):
    pass

def chocAnMenu(dataRepository : DataRepository):
    choice = -1
    menuOptions = \
        ["Interactive Mode",\
        "Generate Reports",\
        "Return to user mode selection."]
    endOption = len(menuOptions)
    while choice != endOption:
        print("What subsystem would you like to use?")
        choice = helperFunctions.menuManager(menuOptions)
        if choice == 1:
            interactiveMode.interactiveMode(dataRepository)
        elif choice == 2:
            pass
    return

if __name__ == "__main__":
    main()