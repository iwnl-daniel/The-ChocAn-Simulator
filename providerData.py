import helperFunctions
import random

#This file contains the classes Provider and ProviderData which
#makes up the part of the data repository concerning provider information.

#The Provider class contains all personal information of one provider.
class Provider:
    #The constructor is the only time the provider number is
    #allowed to be set.
    def __init__(self, number : int):
        self.providerName = None
        self.providerNumber = number
        self.providerAddress = None
        self.providerCity = None
        self.providerState = None
        self.providerZip = None
    #Return true if any of the fields besides providerNumber are already filled.
    def checkFilled(self) -> bool:
        if self.providerName or self.providerAddress or self.providerCity or\
            self.providerState or self.providerZip:
            return True
        return False
    #Fills all of the fields of the class except for providerNumber.
    #Returns false and does not do anything if any of the fields are already filled.
    #Returns true otherwise.
    def fillProvider(self) -> bool:
        if self.checkFilled() == True:
            return False
        self.providerName = helperFunctions.informationPrompter("provider's name", 1, 25)
        self.providerAddress = helperFunctions.informationPrompter("provider's address", 1, 25)
        self.providerCity = helperFunctions.informationPrompter("provider's city", 1, 14)
        self.providerState = helperFunctions.informationPrompter("provider's state", 2, 2)
        self.providerZip = helperFunctions.informationPrompter("provider's zip code", 5, 5)
    #Displays through all fields aside providerNumber and asks the user if they would like to
    #change them, then lets the user do so.
    #Returns false and does nothing if none of the fields are filled yet.
    #Otherwise, returns true.
    def adjustProvider(self) -> bool:
        if self.checkFilled() == False:
            return False
        if self.providerName:
            print("The current provider name is: " + self.providerName + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.providerName = helperFunctions.informationPrompter("provider's name", 1, 25)
        if self.providerAddress:
            print("The current provider address is: " + self.providerAddress + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.providerAddress = helperFunctions.informationPrompter("provider's address", 1, 25)
        if self.providerCity: 
            print("The current provider city is: " + self.providerCity + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.providerCity = helperFunctions.informationPrompter("provider's city", 1, 14)
        if self.providerState:
            print("The current provider state is: " + self.providerState + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.providerState = helperFunctions.informationPrompter("provider's state", 2, 2)
        if self.providerZip:
            print("The current provider zip code is: " + self.providerZip + ". Do you want to change it?")
            if helperFunctions.yesNoPrompter():
                self.providerZip = helperFunctions.informationPrompter("provider's zip code", 5, 5)

class ProviderData:
    def __init__(self):
        self.providerTable = dict()
        #Range of numbers that area a valid provider number
        self.maxNumber = 999999999
        self.minNumber = 100000000

    #Randomly generates an unused provider number.
    #Seed parameter only exists for unit tests.
    def generateProviderNumber(self, seed=None) -> int:
        random.seed(seed)
        providerNumber = -1
        validNumber = False
        while validNumber == False:
            providerNumber = random.randint(self.minNumber, self.maxNumber)
            if providerNumber not in self.providerTable:
                validNumber = True
        return providerNumber

    #Creates Provider class with valid number, then lets the user fill in the
    #provider information, and then stores the provider in the table.
    def insertProvider(self):
        number = self.generateProviderNumber()
        provider = Provider(number)
        provider.fillProvider()
        self.providerTable[provider.providerNumber] = provider
        print("The provider number is: " + str(number))

    #Takes a provider number as an input and checks if it is in the dictionary.
    #If it is, remove it and remove true.
    #Otherwise, remove false.
    def removeProvider(self, number : int) -> bool:
        if number not in self.providerTable:
            return False
        del self.providerTable[number]
        return True

    def retrieveProvider(self, number : int) -> Provider:
        if number not in self.providerTable:
            return None
        return self.providerTable[number]

    #Validates Provier ID for login access to ChocAn
    def validateProvider(self, number) -> Provider:
        if helperFunctions.validNumberCheck(number):  # checks if number is a 9 digit numerical value
            provider = self.retrieveProvider(int(number))  # searches data repository for existing provider id
            if provider is not None:
                print("Login Successful")
                return provider
    
            else:
                print("Error: Invalid Provider ID")
                return None
    
        else:
            print("Error: Not a valid 9 digit ID")
            return None