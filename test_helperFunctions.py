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

class Test_yesNoErrorCheck:
    def test_yes(self):
        assert helperFunctions.yesNoErrorCheck("yes") == 1
        assert helperFunctions.yesNoErrorCheck("Yes") == 1
        assert helperFunctions.yesNoErrorCheck("y") == 1
        assert helperFunctions.yesNoErrorCheck("Y") == 1
    def test_no(self):
        assert helperFunctions.yesNoErrorCheck("no") == -1
        assert helperFunctions.yesNoErrorCheck("n") == -1
        assert helperFunctions.yesNoErrorCheck("No") == -1
        assert helperFunctions.yesNoErrorCheck("N") == -1
    def test_invalidInput(self):
        assert helperFunctions.yesNoErrorCheck("word") == 0

class Test_memuErrorCheck:
    def test_validChoice(self):
        assert helperFunctions.menuErrorCheck(3, 1, 5) == True
    def test_invalidChoice(self):
        assert helperFunctions.menuErrorCheck(7, 1, 5) == False