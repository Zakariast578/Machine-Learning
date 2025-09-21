import pandas as pd

#Assignment link:
#https://g.co/gemini/share/dbdac4226137


#Metrics
#Use pandas to obtain statistical metrics for data.

#A. Numeric metrics
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
  'yearID': [2016, 2016, 2016, 2016, 2017],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
  'HR': [31, 39, 43, 38, 39],
  'RBI': [113, 101, 105, 127, 110]})

print('{}\n'.format(df))

metrics1 = df.describe()
print('{}\n'.format(metrics1))

hr_rbi = df[['HR','RBI']]
metrics2 = hr_rbi.describe()
print('{}\n'.format(metrics2))

#B. Categorical features#
p_ids = df['playerID']
print('{}\n'.format(p_ids.value_counts()))

print('{}\n'.format(p_ids.value_counts(normalize=True)))

print('{}\n'.format(p_ids.value_counts(ascending=True)))

unique_players = df['playerID'].unique()
print('{}\n'.format(repr(unique_players)))

unique_teams = df['teamID'].unique()
print('{}\n'.format(repr(unique_teams)))