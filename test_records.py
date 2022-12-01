import records
import pytest


@pytest.fixture
def recordsTest():
    recordsList = records.Records()
    return recordsList


def test_addRecord(recordsTest):
    assert recordsTest.addRecord(12012022, 000000, 111111, 222222222, "comment example") == True





