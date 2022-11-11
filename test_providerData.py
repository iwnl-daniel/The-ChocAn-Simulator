import providerData
import pytest

@pytest.fixture
def emptyProvider():
    provider = providerData.Provider(0)
    return provider

@pytest.fixture
def filledProvider():
    provider = providerData.Provider(111111111)
    provider.providerAddress = "Home Street"
    provider.providerCity = "Home City"
    provider.providerName = "John"
    provider.providerState = "OR"
    provider.providerZip = 11111
    return provider

def test_checkFilled(emptyProvider, filledProvider):
    assert emptyProvider.checkFilled() == False
    assert filledProvider.checkFilled() == True

@pytest.fixture
def providerDataTest():
    providerDataNumber = providerData.ProviderData()
    return providerDataNumber

class Test_providerData():
    def test_generateProviderNumber(self, providerDataTest):
        seed = 5
        generatedNumber = providerDataTest.generateProviderNumber(seed)
        assert generatedNumber >= providerDataTest.minNumber 
        assert generatedNumber <= providerDataTest.maxNumber
    def test_removeProvider(self, providerDataTest, filledProvider):
        providerDataTest.providerTable[filledProvider.providerNumber] = filledProvider
        #Check for correct output when non-existant provider is used as an input
        assert providerDataTest.removeProvider(333333333) == False
        #Check that valid input has correct output and actually removes the provider
        assert providerDataTest.removeProvider(filledProvider.providerNumber) == True
        assert filledProvider.providerNumber not in providerDataTest.providerTable
    def test_retrieveProvider(self, providerDataTest, filledProvider):
        providerDataTest.providerTable[filledProvider.providerNumber] = filledProvider
        #Check for correct output when non-existant provider is used as an input
        assert providerDataTest.retrieveProvider(333333333) == None
        #Check that valid input retrieve the provider
        retrievedProvider = providerDataTest.retrieveProvider(filledProvider.providerNumber)
        assert retrievedProvider == filledProvider