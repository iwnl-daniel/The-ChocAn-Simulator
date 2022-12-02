from records import Records
#from dataRepository import DataRepository
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
        self.read()

    def read(self) -> bool:
        with open('providerDirectory.csv', 'r') as external_file:
            reader = csv.reader(external_file)

            for line in reader:
                self.dictionary[line[0]] = line[1], line[2]
        
        # self.dictionary should have all the info from the .csv file now

    def viewDirectory(self):
        for i, j in self.dictionary.items():
            print(i, ":", j)
        print("\n")