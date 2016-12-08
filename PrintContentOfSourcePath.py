import sys
import os

inReadMode = 'r'
helpMessage = 'Please pass source and destiny path'
sourcePathIdx = 1
destinyPathIdx = 2
minAmmOfArgs = 1
properAmmOfArgs = 3

def printWhatIsInSourcePath(stdInput):
    if len(stdInput) == properAmmOfArgs:
        properSourcePath = os.path.normpath(stdInput[sourcePathIdx])
        print os.listdir(properSourcePath)

printWhatIsInSourcePath(sys.argv)
