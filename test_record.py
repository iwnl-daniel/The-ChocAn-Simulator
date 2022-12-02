import record
import pytest


@pytest.fixture
def filledRecord():
    record1 = record.Record(11302022, 111111, 222222, 333333333, "comment example")
    return record1

def test_display_record(filledRecord):
    if filledRecord.displayRecord() == True:
        assert True

    else:
        assert False
