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
    member.memberName = "Member"
    member.memberState = "OR"
    member.memberZip = 11111
    return member

def test_checkFilled(emptyMember, filledMember):
    assert emptyMember.checkFilled() == False
    assert filledMember.checkFilled() == True