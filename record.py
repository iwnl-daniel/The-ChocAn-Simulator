import helperFunctions
from datetime import datetime

#  this file contains the Record class which contains the data members for a summary report


class Record:

    # constructor
    def __init__(self, serviceDate, providerNumber : int, memberNumber : int, serviceCode : int, comments):
        self.serviceDate = serviceDate
        self.providerNumber = providerNumber
        self.memberNumber = memberNumber
        self.serviceCode = serviceCode
        self.comments = comments


    def displayRecord(self): # prints out all data members of Record class
        currentTime = datetime.now()
        currentTimeString = currentTime.strftime("%m/%d/%Y %H:%M:%S")
        print("Current Date:", currentTimeString)
        print("Service Date:", self.serviceDate)
        print("Provider Number:", self.providerNumber)
        print("Member Number:", self.memberNumber)
        print("Service Code:", self.serviceCode)
        print("Comments:", self.comments)
        return True


    def displayMemberRecord(self):  # prints out required information for a member record
        print("Date of Service:", self.serviceDate)
        print("Provider Number:", self.providerNumber)
        print("Service Code:", self.serviceCode)


    def displayProviderRecord(self):  # prints out required information for a provider record
        currentTime = datetime.now()
        currentTimeString = currentTime.strftime("%m/%d/%Y %H:%M:%S")
        print("Current Date:", currentTimeString)
        print("Date of Service:", self.serviceDate)
        print("Member Number:", self.memberNumber)
        print("Service Code:", self.serviceCode)
        #  missing fees, # of consultations, total fees
