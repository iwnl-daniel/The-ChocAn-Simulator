import helperFunctions
from memberData import MemberData
from record import Record

class Records(MemberData):

    # constructor
    def __init__(self):
        super().__init__()
        self.database = []  # Records will start out with an empty database


    def addRecord(self, currentDate, serviceDate, providerNumber : int, memberNumber : int, serviceCode : int, comments):
        self.database.append(Record(currentDate, serviceDate, providerNumber, memberNumber, serviceCode, comments))
        return True

