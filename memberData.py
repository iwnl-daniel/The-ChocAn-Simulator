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
    def fillMember(self) -> bool:
        pass