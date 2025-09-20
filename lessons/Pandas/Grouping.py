import pandas as pd

#link to assignment:
# #https://g.co/gemini/share/8c906280d125

#Grouping DataFrames

#A. Grouping by column#
# Predefined df of MLB stats
#create sample df 

df = pd.DataFrame({'yearID': [2017, 2015, 2016, 2015, 2016, 2016, 2015, 2017, 2017],
                   'teamID': ['CLE', 'CLE', 'BOS', 'DET', 'DET', 'CLE', 'BOS', 'BOS', 'DET'],
                   'H': [1449, 1395, 1598, 1515, 1476, 1435, 1495, 1461, 1435],
                   'R': [818, 669, 878, 689, 750, 777, 748, 785, 735]})

print('{}\n'.format(df))

groups = df.groupby('yearID')
for name, group in groups:
  print('Year: {}'.format(name))
  print('{}\n'.format(group))
  
print('{}\n'.format(groups.get_group(2016)))
print('{}\n'.format(groups.sum()))
print('{}\n'.format(groups.mean()))

no2015 = groups.filter(lambda x: x.name > 2015)
print(no2015)

#B. Multiple columns#
groups = df.groupby(['yearID', 'teamID'])
for name, group in groups:
  print('Year and Team: {}'.format(name))
  print('{}\n'.format(group))
  
print('{}\n'.format(groups.sum()))
