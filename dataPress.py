"""
Created on Fri May 26 12:00:17 2017
@author: Ian
"""

f = open('/reg/g/psdm/data/ExpNameDb/experiment-db.dat', 'r')
a = f.read()
f.close()

cTemplate = open("cTemplate.txt","r")
newCFile = cTemplate.read()
cTemplate.close()


g = open('template.py')
apple = g.read()
g.close()


f = open("/reg/g/psdm/data/ExpNameDb/experiment-db.dat", "r")
dataLines = f.readlines()
newlineRemoved = []
for line in dataLines:
    new = line.replace('\n','') 
    new = new.replace('\r','')
    newlineRemoved.append(new)
    art = line.rstrip(' ') + '    '
    a = a.replace(line,art)
f.close()

cFormattedData = ""

for line in newlineRemoved:
    cFormattedData = cFormattedData + line  + "\\n"


dataLength = str(len(cFormattedData))

newCFile = newCFile.replace('DATASIZE',dataLength)



newCFile = newCFile.replace('STRING',cFormattedData)

cFile = open("updatedCFile.c","w")

cFile.write(newCFile)

cFile.close()

pear = apple.replace('STRING', a)

h = open('ExpNameData.py', 'w')
h.write(pear)
h.close()

#expno = {}
#with open('C:\Users\Ian\Desktop\ExperimentData.txt') as e:
#    for line in e:
#        splitLine = line.split()
#        expno[int(splitLine[0])] = ','.join(splitLine[1:])
#e.close()
