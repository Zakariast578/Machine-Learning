import pandas as pd
import matplotlib.pyplot as plt

#Assignment link:
#https://g.co/gemini/share/b6f819d842e6

#Plotting
#Use pandas to create plots for data.

#A. Basic plots
data = {'yearID': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007],
        'HR': [49, 73, 46, 45, 45, 5, 26, 28]}
df = pd.DataFrame(data)

df.plot(kind='line',x='yearID',y='HR')
plt.show()

# predefined df
print('{}\n'.format(df))

df.plot(kind='line',x='yearID',y='HR')
plt.show()
# plt.savefig('output/legend.png')  # save to PNG file

# predefined df
print('{}\n'.format(df))

df.plot(kind='line',x='yearID',y='HR')
plt.title('HR vs. Year')
plt.xlabel('Year')
plt.ylabel('HR Count')
plt.show()

#B. Other plots #
# predefined df
# print('{}\n'.format(df))

df.plot(kind='bar',y='HR')
plt.ylabel('Frequency')
plt.show()

#C. Multiple features #
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
  'yearID': [2016, 2016, 2016, 2016, 2017],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
  'HR': [31, 39, 43, 38, 39],
  'RBI': [113, 101, 105, 127, 110]})

# predefined df
print('Multiple Features DataFrame:')

# gca stands for 'get current axis'
ax = plt.gca()

df.plot(kind='line',x='yearID',y='HR',ax=ax)
df.plot(kind='line',x='yearID',y='RBI', color='red', ax=ax)
plt.show()