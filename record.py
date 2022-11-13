import helperFunctions
from datetime import datetime

class Record:

    # constructor
    def __init__(self, currentDate, serviceDate, providerNumber : int, memberNumber : int, serviceCode : int, comments):
        self.currentDate = currentDate
        self.serviceDate = serviceDate
        self.providerNumber = providerNumber
        self.memberNumber = memberNumber
        self.serviceCode = serviceCode
        self.comments = comments


    def displayRecord(self): # prints out all data members of Record class
        print("Current Date:", self.currentDate)
        print("Service Date:", self.serviceDate)
        print("Provider Number:", self.providerNumber)
        print("Member Number:", self.memberNumber)
        print("Service Code:", self.serviceCode)
        print("Comments:", self.comments)


   # def displayMemberRecord(self):


   # def displayProviderRecord(self):


   # def retrieveMember(self, number : int):
