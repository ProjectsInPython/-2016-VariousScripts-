import sys
import os

inReadMode = 'r'
helpMessage = 'Please pass source and destiny path'
sourcePathIdx = 1
destinyPathIdx = 2
minAmmOfArgs = 1
properAmmOfArgs = 3

def iterateOverSourcePath(stdInput):
    if len(stdInput) == properAmmOfArgs:
        properSourcePath = os.path.normpath(stdInput[sourcePathIdx])

        for file in os.listdir(properSourcePath):
            print file

iterateOverSourcePath(sys.argv)
