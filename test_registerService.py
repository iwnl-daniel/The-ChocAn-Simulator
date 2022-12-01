# This file contains tests for the registerService file
import registerService
# === registerService function tests ===






# === displayService function tests ===

# Test: invalid user input for service number
def test_displayService_invalid_userInput(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    value = registerService.displayService('123456')
    assert value == False
    value = registerService.displayService('213121')
    assert value == False
    value = registerService.displayService('918321')
    assert value == False
# Test: valid user input for service number
def test_displayService_valid_userInput(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    value = registerService.displayService('175932')
    assert value == True
    value = registerService.displayService('741960')
    assert value == True
    value = registerService.displayService('583667')
    assert value == True
# Test: user can enter either all of the following:
# y, Y, yes (in any form of capitalization),
# n, N, no (in any form of capitalization)
# when asked if service number matches what they entered 
def test_userInput_correct_service_question(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    value = registerService.displayService('175932')
    assert value == True
    monkeypatch.setattr('builtins.input', lambda _: "Y")
    value = registerService.displayService('175932')
    assert value == True
    monkeypatch.setattr('builtins.input', lambda _: "YES")
    value = registerService.displayService('175932')
    assert value == True
    monkeypatch.setattr('builtins.input', lambda _: "yes")
    value = registerService.displayService('175932')
    assert value == True
    monkeypatch.setattr('builtins.input', lambda _: "yEs")
    value = registerService.displayService('175932')
    assert value == True
    monkeypatch.setattr('builtins.input', lambda _: "n")
    value = registerService.displayService('175932')
    assert value == False
    monkeypatch.setattr('builtins.input', lambda _: "N")
    value = registerService.displayService('175932')
    assert value == False
    monkeypatch.setattr('builtins.input', lambda _: "no")
    value = registerService.displayService('175932')
    assert value == False
    monkeypatch.setattr('builtins.input', lambda _: "NO")
    value = registerService.displayService('175932')
    assert value == False
    monkeypatch.setattr('builtins.input', lambda _: "nO")
    value = registerService.displayService('175932')
    assert value == False

  

# Test 

# Test 

# Test 

# Test 





