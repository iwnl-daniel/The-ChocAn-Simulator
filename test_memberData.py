import memberData
import pytest

@pytest.fixture
def emptyMember():
    member = memberData.Member(0)
    return member

@pytest.fixture
def filledMember():
    member = memberData.Member(111111111)
    member.memberAddress = "Home Street"
    member.memberCity = "Home City"
    member.memberName = "John"
    member.memberState = "OR"
    member.memberZip = 11111
    return member

def test_checkFilled(emptyMember, filledMember):
    assert emptyMember.checkFilled() == False
    assert filledMember.checkFilled() == True

@pytest.fixture
def memberDataTest():
    memberDataNumber = memberData.MemberData()
    return memberDataNumber

class Test_memberData():
    def test_generateMemberNumber(self, memberDataTest):
        seed = 5
        generatedNumber = memberDataTest.generateMemberNumber(seed)
        assert generatedNumber >= memberDataTest.minNumber 
        assert generatedNumber <= memberDataTest.maxNumber
    def test_removeMember(self, memberDataTest, filledMember):
        memberDataTest.memberTable[filledMember.memberNumber] = filledMember
        #Check for correct output when non-existant member is used as an input
        assert memberDataTest.removeMember(333333333) == False
        #Check that valid input has correct output and actually removes the member
        assert memberDataTest.removeMember(filledMember.memberNumber) == True
        assert filledMember.memberNumber not in memberDataTest.memberTable
    def test_retrieveMember(self, memberDataTest, filledMember):
        memberDataTest.memberTable[filledMember.memberNumber] = filledMember
        #Check for correct output when non-existant member is used as an input
        assert memberDataTest.retrieveMember(333333333) == None
        #Check that valid input retrieve the member
        retrievedMember = memberDataTest.retrieveMember(filledMember.memberNumber)
        assert retrievedMember == filledMember