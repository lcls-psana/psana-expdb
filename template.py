# 'data' organized as [Experiment No., Hutch, Experiment Name]

data = '''STRING'''

rows = data.split('\n')
ExpNo = {}
for row in rows:
    vals = row.split()
    ExpNo[vals[0]] = (vals[1], vals[2])
