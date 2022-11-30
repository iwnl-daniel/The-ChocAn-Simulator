from records import Records
from dataRepository import DataRepository
import helperFunctions
import csv

# This file is responsible for the functions of the provider directory

# This reads in information from a .csv file (providerDirectory.csv) which contains the provider information.
# Said information includes: The name of the actual provider occupation, their service code, and their fee.
# Note: Within the .csv file, these are denoted as: service,code,fee
# Said information is then stored in a dictionary data structure

# An entry in the dictionary that holds the service, code, and fee
# class DirectoryEntry:
#     def __init__(self):
#         self.service = None
#         self.code = None
#         self.fee = None

class Directory(Records):

    def __init__(self):
        super().__init__()
        self.dictionary = dict()

    def read(self) -> bool:
        with open('providerDirectory.csv', 'r') as external_file:
            reader = csv.reader(external_file)

            for line in reader:
                self.dictionary[line[0]] = line[1], line[2]
        
        # self.dictionary should have all the info from the .csv file now

    def viewDirectory(self):
        print("Directory here\n")
        pass

def directoryInterface(dataRepository : DataRepository):
    choice = -1
    menuOptions = \
        ["View Provider Directory.",\
        "Return to previous menu."]
    endOption = len(menuOptions)
    while choice != endOption:
        print("What would you like to do?")
        choice = helperFunctions.menuManager(menuOptions)
        if choice == 1:
            directory = Directory()
            directory.viewDirectory()
    return