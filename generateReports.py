from dataRepository import DataRepository
import helperFunctions


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
    memberReport = dataRepository.retrieveAllMemberRecords()
    if not memberReport:
        print("No records found in database")
        return
    else:
        print("Members found:") #partially implemented, need ability to create records for further development
        for i in range(len(memberReport)):
            print("Member number:", memberReport[i].memberNumber)
        return
    return


def providerReport(dataRepository : DataRepository, providerNumber):
    summaryReport = dataRepository.retrieveProviderRecords(int(providerNumber))
    if not summaryReport:
        print("No records found for specified provider number")
        return

    else:
        with open(f'providerReport_{providerNumber}.txt', 'w') as f:
            for i in range(len(summaryReport)):
                f.write(summaryReport[i].displayProviderRecord())  # reimplementation/testing required?
                f.write("\n\n")

            print("Provider Report Generated for Provider", providerNumber)
            return

# manager report is a collection of provider reports for all providers to be used by a manager
def managerReport(dataRepository : DataRepository):
    recordNumbers = dataRepository.returnProviderRecords()
    for i in range(len(recordNumbers)):
        providerReport(recordNumbers[i])
    return
