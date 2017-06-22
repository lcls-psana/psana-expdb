# 'data' organized as [Experiment No., Hutch, Experiment Name]

data = '''STRING'''

data = data.replace("	", "    ")
data = data[:-1]
rows = data.split('\n')
ExpNo = {}
for row in rows:
    vals = row.split()
    ExpNo[vals[0]] = (vals[1], vals[2])
