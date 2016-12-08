import sys
import os

helpMessage = 'Please pass source and destiny path'
ammountOfArgs = len(sys.argv)
sourcePathIdx = 1
destinyPathIdx = 2
minAmmOfArgs = 1
properAmmOfArgs = 3

if ammountOfArgs == properAmmOfArgs:
    print os.path.normpath(sys.argv[sourcePathIdx])
    print os.path.normpath(sys.argv[destinyPathIdx])
else:
    print helpMessage
