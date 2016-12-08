import sys
import os
import shutil

inReadMode = 'r'
helpMessage = 'Please pass source and destiny path'
sourcePathIdx = 1
destinyPathIdx = 2
minAmmOfArgs = 1
properAmmOfArgs = 3

def copyFileSrcToDst(stdInput, pathDst):
    properSourcePath = os.path.normpath(stdInput)
    properDestinyPath = os.path.normpath(pathDst)
    shutil.copy(stdInput, properDestinyPath)

def copyFolderSrcToDst(stdInput):
    if len(stdInput) == properAmmOfArgs:
        properSourcePath = os.path.normpath(stdInput[sourcePathIdx])

        print stdInput[sourcePathIdx]
        #print os.listdir(properSourcePath)
        #for file in os.listdir(properSourcePath):
            #print file
            #copyFileSrcToDst(os.path.abspath(file), sys.argv[2])

copyFolderSrcToDst(sys.argv)
