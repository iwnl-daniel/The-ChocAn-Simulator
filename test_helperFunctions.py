import helperFunctions

#Unit testing for helperFunctions.py

class Test_stringLengthCheck:
    def test_inBounds(self):
        #string length within bounds
        assert helperFunctions.stringLengthCheck("string",3,7) == 0
        #string on bounds
        assert helperFunctions.stringLengthCheck("string",6,6) == 0
        assert helperFunctions.stringLengthCheck("string",6,7) == 0
        assert helperFunctions.stringLengthCheck("string",5,6) == 0
    def test_outOfBounds(self):
        #string out of bounds
        assert helperFunctions.stringLengthCheck("string",7,10) == -1
        assert helperFunctions.stringLengthCheck("string",1,3) == 1

class Test_yesNoChecker:
    def test_yes(self):
        assert helperFunctions.yesNoChecker("yes") == 1
        assert helperFunctions.yesNoChecker("Yes") == 1
        assert helperFunctions.yesNoChecker("y") == 1
        assert helperFunctions.yesNoChecker("Y") == 1
    def test_no(self):
        assert helperFunctions.yesNoChecker("no") == -1
        assert helperFunctions.yesNoChecker("n") == -1
        assert helperFunctions.yesNoChecker("No") == -1
        assert helperFunctions.yesNoChecker("N") == -1
    def test_invalidInput(self):
        assert helperFunctions.yesNoChecker("word") == 0