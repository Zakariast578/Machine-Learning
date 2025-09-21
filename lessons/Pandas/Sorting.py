import pandas as pd

#Assignment link:
#https://g.co/gemini/share/dbdac4226137

#Sorting

#A. Sorting by feature#
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
  'yearID': [2016, 2016, 2016, 2016, 2017],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
  'HR': [31, 39, 43, 38, 39]})

print('{}\n'.format(df))

sort1 = df.sort_values('yearID')
print('{}\n'.format(sort1))

sort2 = df.sort_values('playerID', ascending=False)
print('{}\n'.format(sort2))

# df is predefined
print('{}\n'.format(df))

sort1 = df.sort_values(['yearID', 'playerID'])
print('{}\n'.format(sort1))

sort2 = df.sort_values(['yearID', 'HR'],
                       ascending=[True, False])
print('{}\n'.format(sort2))