'''
Created on Feb 21, 2021

@author: Aneep
'''
import csv, os, glob
from enum import IntEnum

# make an enum of Enrollment data points and their position in a CSV line
class EnrollIndex(IntEnum):
    UID = 0
    FNAME = 1
    LNAME = 2
    VERS = 3
    COMPANY = 4
# dictionary to hold <K,V> of insurance company name (string) to 
# every member (list of tuples) enrolled in that company
csvDict = {}

# simple logic just to get the file path of the input dir
here = (os.path.dirname(os.path.abspath(__file__)))
inputDir = os.path.join(here, 'input\\')
outputDir = os.path.join(here, 'output\\')

# Function to sort the list of tuples by name
# 
# returns a list of tuples, sorted by name ascending
def sortTuples(tup):
    return sorted(tup, key = lambda x: x[EnrollIndex.FNAME])

# Function to check and see if the UID already exists in the company's enrollee tuple
def uidExists(csvDict, uid, strCompany):
    return (list(filter(lambda x: x.count(uid) > 0, csvDict[strCompany])))
        
# Function which will take the sorted and completed dict and write each entry
# into its own file, with the file names being the value of the Key
#
# This will also sort the list of tuples in the dict, since we're already iterating through the whole thing
def writeDictToOutput():
    for key in csvDict:
        csvDict[key] = (sortTuples(csvDict[key]))
        outFilePath = os.path.join(outputDir, (key + ".csv"))
        
        outFile = open(outFilePath, "w")
        print("WRITING TO :: ", outFile.name)
        for userTuple in csvDict[key]:
            print("USER TUPLE :: ", userTuple)
            outFile.write(str(userTuple) + "\n")
        outFile.close()    


# loop through every CSV file in the input dir, and then operate on the csvDict
for csvName in glob.glob(inputDir + '*.csv'):
    with open(csvName, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # convert the array of chars to a string
            strCompany = "".join(row[EnrollIndex.COMPANY]) 
            # make a tuple of the rest of the information for an enrollee
            userTuple = tuple(row[EnrollIndex.UID:EnrollIndex.COMPANY])  
            
            
            # check and see if the company is already in the dict, if so add to its tuple
            # we will also make sure to check if the User ID already exists in the tuple list
            if strCompany in csvDict:
                #print(strCompany + " is in the dict")
                # check and see if the User ID exists in the tuple list for this company
                matchList = uidExists(csvDict, userTuple[EnrollIndex.UID], strCompany)
                # User ID exists. matchList is a list of tuples, so we need to reference the [0] index
                if matchList != []:
                    #print ("User ID Match found: ", matchList[0][EnrollIndex.UID])
                    # find the index in the list of tuples in csvDict
                    matchIndex = csvDict[strCompany].index(matchList[0])
                    if (csvDict[strCompany][matchIndex][EnrollIndex.VERS]) <= userTuple[EnrollIndex.VERS]:
                        #print("the new version was higher")
                        # new version is higher, so replace the previous tuple with the current one
                        csvDict[strCompany][matchIndex] = userTuple
                    else:
                        print("the new version was not higher")
                else:
                    # there was no match, so just concatenate the current enrollee tuple to
                    # what we already have for this company
                    csvDict[strCompany] = csvDict[strCompany] + [userTuple]
            else:
                # the company is not already in our dict, so simply add it
                csvDict[strCompany] = [userTuple]
        
        for key in csvDict:
            csvDict[key] = (sortTuples(csvDict[key]))
writeDictToOutput()