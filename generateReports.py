from dataRepository import DataRepository
import helperFunctions
from datetime import datetime


def generateReports(dataRepository : DataRepository):
    choice = -1
    menuOptions = \
        ["Generate Member Report",\
        "Generate Provider Report",\
        "Generate Manager Report",\
        "Return to previous menu"]
    endOption = len(menuOptions)
    while choice != endOption:
        print("What would you like to do?")
        choice = helperFunctions.menuManager(menuOptions)
        if choice == 1:
            memberReport(dataRepository)
        elif choice == 2:
            print("Please enter a Provider Number:")
            number = input()
            providerReport(dataRepository, number)
        elif choice == 3:
            managerReport(dataRepository)
    return


def memberReport(dataRepository : DataRepository):
    for i in range(len(dataRepository.database)):
        if(dataRepository.checkIfMemberHasRecord(dataRepository.database[i].memberNumber)):
            member = dataRepository.retrieveMember(int(dataRepository.database[i].memberNumber))
            with open(f'memberReport_{member.memberNumber}.txt', 'a') as f:  # Writes to a txt file with name 'memberReport_<memberNumber>.txt'
                currentTime = datetime.now()
                currentTimeString = currentTime.strftime("%m/%d/%Y %H:%M:%S")
                f.write('Current Date: ')
                f.write(currentTimeString)
                f.write('\n\n')
                print("Member name:", member.memberName, file=f)
                print("Member number:", member.memberNumber, file=f)
                print("Member address:", member.memberAddress, file=f)
                print("Member city:", member.memberCity, file=f)
                print("Member state:", member.memberState, file=f)
                print("Member zip code:", member.memberZip, file=f)
                print("\n", file=f)
                memberRecords = dataRepository.retrieveMemberRecords(str(member.memberNumber))
                for i in range(len(memberRecords)):
                    print("Date of Service:", memberRecords[i].serviceDate, file=f)
                    print("Provider Number:", memberRecords[i].providerNumber, file=f)
                    print("Service Code:", memberRecords[i].serviceCode, file=f)
        else:
            print(dataRepository.database[i].memberNumber, "has no records")
    return


def providerReport(dataRepository : DataRepository, providerNumber):
    summaryReport = dataRepository.retrieveProviderRecords(providerNumber)
    if not summaryReport:
        print("No records found for specified provider number")
        return

    else:
        with open(f'providerReport_{providerNumber}.txt', 'a') as f:  # Writes to a txt file with name 'providerReport_<providerNumber>.txt'
            currentTime = datetime.now()
            currentTimeString = currentTime.strftime("%m/%d/%Y %H:%M:%S")
            f.write('Current Date: ')
            f.write(currentTimeString)
            f.write('\n\n')

            for i in range(len(summaryReport)):
                print("Date of Service:", summaryReport[i].serviceDate, file=f)
                print("Member Number:", summaryReport[i].memberNumber, file=f)
                print("Service Code:", summaryReport[i].serviceCode, file=f)
                print("\n", file=f)

        print("Provider Report Generated for Provider", providerNumber)
        return

# manager report is a collection of provider reports for all providers to be used by a manager
def managerReport(dataRepository : DataRepository):
    recordNumbers = dataRepository.returnProviderRecords()
    for i in range(len(recordNumbers)):
        providerReport(dataRepository, recordNumbers[i])
    return
