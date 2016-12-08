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
    shutil.copy(properSourcePath, properDestinyPath)

copyFileSrcToDst(sys.argv[1]+ r'\Utils.hpp', sys.argv[2])
