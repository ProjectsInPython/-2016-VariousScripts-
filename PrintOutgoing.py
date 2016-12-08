import os
import re

loglinep = r'ALMAG: Outgoing::*'
parsedLogs = open('D:/alumag_MasterOnVS/alumag/korytko/Data/DataParsed.txt', 'w')
logPath = ''
with open(logPath, "r") as logfile:
    for line in logfile:
        checked = re.search(loglinep, line)
        if checked:
            parsedLogs.write(line);

# Close opend file
logfile.close()
parsedLogs.close()
