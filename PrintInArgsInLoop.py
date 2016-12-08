import sys
import os

inReadMode = 'r'
helpMessage = 'Please pass source and destiny path'
ammountOfArgs = len(stdInput)
sourcePathIdx = 1
destinyPathIdx = 2
minAmmOfArgs = 1
properAmmOfArgs = 3

def printProperPath(stdInput):
    if ammountOfArgs == properAmmOfArgs:
        print os.path.normpath(stdInput[sourcePathIdx])
        print os.path.normpath(stdInput[destinyPathIdx])
    else:
        print helpMessage

def printWhatIsInSourcePath(stdInput):


    if ammountOfArgs == properAmmOfArgs:
        print os.path.normpath(stdInput[sourcePathIdx])
        print os.path.normpath(stdInput[destinyPathIdx])
    else:
        print helpMessage

    with open(stdInput[sourcePathIdx], inReadMode) as generatedMeta:
        print 'Siema'

printWhatIsInSourcePath(sys.argv)


