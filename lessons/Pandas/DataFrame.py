import pandas as pd
import numpy as np

#link to assignment:
#https://g.co/gemini/share/efe25b9ca221

#DataFrame Creation

#A. 2-D data#
df = pd.DataFrame()
# Newline added to separate DataFrames
print('{}\n'.format(df))

df = pd.DataFrame([5, 6])
print('{}\n'.format(df))

df = pd.DataFrame([[5,6]])
print('{}\n'.format(df))

df = pd.DataFrame([[5, 6], [1, 3]],
                  index=['r1', 'r2'],
                  columns=['c1', 'c2'])
print('{}\n'.format(df))

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4]},
                  index=['r1', 'r2'])
print('{}\n'.format(df))

#B. Upcasting#
upcast = pd.DataFrame([[5, 6], [1.2, 3]])
print('{}\n'.format(upcast))
# Datatypes of each column
print(upcast.dtypes)

#C. Appending rows#
df = pd.DataFrame([[5, 6], [1.2, 3]])
ser = pd.Series([0, 0], name='r3', index=[0, 1])

print("--- Original DataFrame ---")
print(df)
print("\n--- Original Series ---")
print(ser)

df_appended_series = pd.concat([df, ser.to_frame().T], ignore_index=True)
print("\n--- Appending a Series as a new row using pd.concat() ---")
print(df_appended_series)

df2 = pd.DataFrame([[0, 0], [9, 9]])
df_appended_df = pd.concat([df, df2], ignore_index=True)
print("\n--- Appending a DataFrame using pd.concat() ---")
print(df_appended_df)

#D. Dropping data#
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]},
                  index=['r1', 'r2'])
# Drop row r1
df_drop = df.drop(labels='r1')
print('{}\n'.format(df_drop))

# Drop columns c1, c3
df_drop = df.drop(labels=['c1', 'c3'], axis=1)
print('{}\n'.format(df_drop))

df_drop = df.drop(index='r2')
print('{}\n'.format(df_drop))

df_drop = df.drop(columns='c2')
print('{}\n'.format(df_drop))

df_drop = df.drop(index='r2', columns='c2')
print('{}\n'.format(df_drop))