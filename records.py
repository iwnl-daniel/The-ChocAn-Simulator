import helperFunctions
from memberData import MemberData
from record import Record

#  this file contains the Records class which contains a list of the Record class data type


class Records(MemberData):

    # constructor
    def __init__(self):
        super().__init__()
        self.database = []  # Records will start out with an empty database

    # add a record into the system's database by invoking the Record constructor
    def addRecord(self, serviceDate, providerNumber : int, memberNumber : int, serviceCode : int, comments):
        self.database.append(Record(serviceDate, providerNumber, memberNumber, serviceCode, comments))
        return True


    # searches and retrieves all records pertaining to member ID (number); returns a list
    def retrieveMemberRecords(self, number : int):
        recordList = []

        for i in range(len(self.database)):
            if self.database[i].memberNumber == number:
                recordList.append(self.database[i])

            return recordList


    # searches and retrieves all records pertaining to provider ID (number); returns a list
    def retrieveProviderRecords(self, number: int):
        recordList = []

        for i in range(len(self.database)):
            if self.database[i].providerNumber == number:
                recordList.append(self.database[i])

            return recordList