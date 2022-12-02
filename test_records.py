import records
import pytest


@pytest.fixture
def recordsTest():
    recordsList = records.Records()
    return recordsList


def test_addRecord(recordsTest):
    assert recordsTest.addRecord(12012022, '111111111', '111111111', 222222, "comment example") == True
    assert recordsTest.addRecord(12012022, 'abcdef', 'characters', 222222, "comment example") == False




