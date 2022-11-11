import memberData

#This file will be where the program is run from, and it
#will be in charge of controlling the flow of the program.

class DataRepository(memberData.MemberData):
    pass

def main():
    dataRepository = DataRepository()

if __name__ == "__main__":
    main()