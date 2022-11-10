import helperFunctions

#This file contains the classes Member and MemberData which
#makes up the part of the data repository concerning member information.

#The Member class contains all personal information of one member.
class Member:
    #The constructor is the only time the member number is
    #allowed to be set.
    def __init__(self, number : int):
        self.memberName = None
        self.memberNumber = number
        self.memberAddress = None
        self.memberCity = None
        self.memberState = None
        self.memberZip = None
    #Return true if any of the fields besides memberNumber are already filled.
    def checkFilled(self) -> bool:
        if self.memberName or self.memberAddress or self.memberCity or\
            self.memberState or self.memberZip:
            return True
        return False
    #Fills all of the fields of the class except for memberNumber.
    #Returns false and does not do anything if any of the fields are already filled.
    #Returns true otherwise.
    def fillMember(self) -> bool:
        if self.checkFilled() == True:
            return False
        self.memberName = helperFunctions.informationPrompter("member's name", 1, 25)
        self.memberAddress = helperFunctions.informationPrompter("member's address", 1, 25)
        self.memberCity = helperFunctions.informationPrompter("member's city", 1, 14)
        self.memberState = helperFunctions.informationPrompter("member's state", 2, 2)
        self.memberZip = helperFunctions.informationPrompter("member's zip code", 5, 5)
    #Displays through all fields aside memberNumber and asks the user if they would like to
    #change them, then lets the user do so.
    #Returns false and does nothing if none of the fields are filled yet.
    #Otherwise, returns true.
    def adjustMember(self) -> bool:
        if self.checkFilled() == False:
            return False
        if self.memberName:
            print("The current member name is: " + self.memberName + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.memberName = helperFunctions.informationPrompter("member's name", 1, 25)
        if self.memberAddress:
            print("The current member address is: " + self.memberAddress + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.memberAddress = helperFunctions.informationPrompter("member's address", 1, 25)
        if self.memberCity: 
            print("The current member city is: " + self.memberCity + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.memberCity = helperFunctions.informationPrompter("member's city", 1, 14)
        if self.memberState:
            print("The current member state is: " + self.memberState + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.memberState = helperFunctions.informationPrompter("member's state", 2, 2)
        if self.memberZip:
            print("The current member zip code is: " + self.memberZip + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.memberZip = helperFunctions.informationPrompter("member's zip code", 5, 5)