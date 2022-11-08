import helperFunctions

#Unit testing for helperFunctions.py

def test_stringLengthError():
    #string length within bounds
    assert helperFunctions.stringLengthError("string",3,7) == 0
    #string on bounds
    assert helperFunctions.stringLengthError("string",6,6) == 0
    assert helperFunctions.stringLengthError("string",6,7) == 0
    assert helperFunctions.stringLengthError("string",5,6) == 0
    #string out of bounds
    assert helperFunctions.stringLengthError("string",7,10) == -1
    assert helperFunctions.stringLengthError("string",1,3) == 1