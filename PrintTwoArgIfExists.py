import sys

idxFstArg = 1
idxSndArg = 2

if len(sys.argv) > 1:
    fstArg = sys.argv[idxFstArg]
    sndArg = sys.argv[idxSndArg]
else:
    fstArg = 'Empty First Arg'
    sndArg = 'Empty Second Arg'

print(fstArg)
print(sndArg)
