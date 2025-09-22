import pandas as pd
import numpy as np

#Assignment link:
#https://g.co/gemini/share/b6f819d842e6


#To NumPy
#Use pandas to convert data to NumPy arrays.

#A. Machine learning#

#B. Indicator features#

# Create a sample DataFrame with a categorical column
data = {'ID': [1, 2, 3, 4],
        'Gender': ['Male', 'Female', 'Female', 'Male'],
        'Age': [25, 30, 22, 40]}
df = pd.DataFrame(data)

print("Original DataFrame:\n{}".format(df))

# Convert the 'Gender' column into indicator features
# The `prefix` argument adds 'Gender' to the new column names
df_encoded = pd.get_dummies(df, columns=['Gender'], prefix='Gender').astype(int)

print("\nDataFrame with Indicator Features:\n{}".format(df_encoded))

numpy_matrix = df_encoded.to_numpy()
print("\nNumPy Array:\n{}".format(numpy_matrix))

#C. Converting to indicators

# Predefined DataFrame (example structure)
data = {'yearID': [2000, 2001, 2002],
        'teamID': ['BOS', 'PIT', 'BOS'],
        'lgID': ['AL', 'NL', 'AL']}
df = pd.DataFrame(data)

print('Original DataFrame:')
print(df)

# Convert all categorical columns to indicator features
converted = pd.get_dummies(df)

print('\nNew DataFrame with indicator features:')
print(converted)

print('\nConverted columns:')
print(converted.columns)

print('\nteamID indicator features:')
print(converted[['teamID_BOS', 'teamID_PIT']])

print('\nlgID indicator features:')
print(converted[['lgID_AL', 'lgID_NL']])

#D. Converting to NumPy#
numpy_matrix = converted.values
print('\nNumPy array:')
print(numpy_matrix)