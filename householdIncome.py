#********************************************************************
#
#  Author:            <Brandon>
#
#  Program #:         10
#
#  File Name:         Program10.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          <Due Date>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter #>
#
#  Description:
#
#********************************************************************
def main():
    developerInfo()
    openInputFile = inputFileOpen()
    count = printRecord(openInputFile)
    averageIncome = Average(openInputFile, count)
    exceedAverage(openInputFile, count, averageIncome)
    percentBelowIncome = povertLevelCalculation(openInputFile, count)
    outputFile(openInputFile, count, averageIncome, percentBelowIncome)
    
def inputFileOpen():    
    inFile = open('program10.txt', 'r')

    acctNum = []
    annualIncome = []
    members = []
    lineRead = inFile.readline()       # Read first record
    while lineRead != '':              # While there are more records
        words = lineRead.split()        # Split the records into substrings
        acctNum.append(int(words[0]))         # Convert first substring to integer
        annualIncome.append(float(words[1]))  # Convert second substring to float
        members.append(int(words[2]))         # Convert third substring to integer
    
        lineRead = inFile.readline()    # Read next record

    # Close the file.
    inFile.close() # Close file
    return acctNum, annualIncome, members

def printRecord(openInputFile):
    print("%12s    %12s  %16s\n" % ("Account #", "Income", "Members"))
    count = 27
    for r in range(count):
        print("%10d   %16.2f   %12d" % (openInputFile[0][r], openInputFile[1][r], openInputFile[2][r]))
    return count


def Average(openInputFile, count):
    totalIncome = 0.0
    for r in range(count):
        totalIncome += openInputFile[1][r]
    averageIncome = totalIncome / count
    print('Average Income: $', format(averageIncome,'.2f'))
    return averageIncome


def exceedAverage(openInputFile, count, averageIncome):
    print('Above Average Income:')
    print("%12s    %12s  %16s\n" % ("Account #", "Income", "Members"))
    for r in range(count):
        if openInputFile[1][r] > averageIncome:
            print("%10d   %16.2f   %12d" % (openInputFile[0][r], openInputFile[1][r], openInputFile[2][r]))

def povertLevelCalculation(openInputFile, count):
    print("Households below poverty line:")
    print("%12s    %12s  %16s\n" % ("Account #", "Income", "Members"))
    householdsBelowIncome = 0
    for r in range(count):
        povertyLevel  = 16460.00 + 4320.00 *  ((openInputFile[2][r]) - 2)
        if openInputFile[1][r] < povertyLevel:
            householdsBelowIncome += 1
            print("%10d   %16.2f   %12d" % (openInputFile[0][r], openInputFile[1][r], openInputFile[2][r]))
    percentBelowIncome = (householdsBelowIncome / count) * 100   
    print('Households below poverty level:', format(percentBelowIncome,'.2f'), '%', sep='')
    return percentBelowIncome
def outputFile(openInputFile, count, averageIncome, percentBelowIncome):
    outFile = open('program10-out.txt', 'w')
    outFile.write(str("%12s    %12s  %16s\n" % ("Account #", "Income", "Members")))

    for r in range(count):
        outFile.write(str("%10d   %16.2f   %12d\n" % (openInputFile[0][r], openInputFile[1][r], openInputFile[2][r])))
    outFile.write(str("Average Income: $"))
    outFile.write(format(averageIncome,'.2f'))
    outFile.write('\n')
    
    outFile.write(str("Above Average Income:\n"))
    outFile.write(str("%12s    %12s  %16s\n" % ("Account #", "Income", "Members")))
    for r in range(count):
        if openInputFile[1][r] > averageIncome:
            outFile.write(str("%10d   %16.2f   %12d\n" % (openInputFile[0][r], openInputFile[1][r], openInputFile[2][r])))
    
    outFile.write(str("Households below poverty line:\n"))
    outFile.write(str("%12s    %12s  %16s\n" % ("Account #", "Income", "Members")))
    for r in range(count):
        povertyLevel  = 16460.00 + 4320.00 *  ((openInputFile[2][r]) - 2)
        if openInputFile[1][r] < povertyLevel:
            outFile.write(str("%10d   %16.2f   %12d\n" % (openInputFile[0][r], openInputFile[1][r], openInputFile[2][r])))
            
    outFile.write(str("Households below poverty level:"))
    outFile.write(format(percentBelowIncome, '.2f',))
    outFile.write(str('%'))
        
def developerInfo():

    print('Name: Brandon Sabrsula')
    print('Course: Programming Fundamentals I')
    print('Program: 9')
    print()

    # End of the developerInfo function
# Call the main function.
main()
