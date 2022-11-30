import helperFunctions
import random
from providerData import ProviderData

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

class MemberData(ProviderData):
    def __init__(self):
        super().__init__()
        self.memberTable = dict()
        #Range of numbers that area a valid member number
        self.maxNumber = 999999999
        self.minNumber = 100000000

    #Randomly generates an unused member number.
    #Seed parameter only exists for unit tests.
    def generateMemberNumber(self, seed=None) -> int:
        random.seed(seed)
        memberNumber = -1
        validNumber = False
        while validNumber == False:
            memberNumber = random.randint(self.minNumber, self.maxNumber)
            if memberNumber not in self.memberTable:
                validNumber = True
        return memberNumber

    #Creates Member class with valid number, then lets the user fill in the
    #member information, and then stores the member in the table.
    def insertMember(self):
        number = self.generateMemberNumber()
        member = Member(number)
        member.fillMember()
        self.memberTable[member.memberNumber] = member
        print("The member number is: " + str(number))

    #Takes a member number as an input and checks if it is in the dictionary.
    #If it is, remove it and remove true.
    #Otherwise, remove false.
    def removeMember(self, number : int) -> bool:
        if number not in self.memberTable:
            return False
        del self.memberTable[number]
        return True

    def retrieveMember(self, number : int) -> Member:
        if number not in self.memberTable:
            return None
        return self.memberTable[number]

    # Validates Member ID for login access to ChocAn
    def validateMember(self, number) -> Member:
        if helperFunctions.validNumberCheck(number):  # checks if number is a 9 digit numerical value
            member = self.retrieveMember(int(number))  # searches data repository for existing member id
            if member is not None:
                print("Login Successful")
                return member

            else:
                print("Error: Invalid Member ID")
                return None

        else:
            print("Error: Not a valid 9 digit ID")
            return None