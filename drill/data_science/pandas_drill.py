import pandas as pd
import numpy as np

use_cols=["Name", "Age", "ID", "Exp"]
df = pd.read_csv(filepath_or_buffer="pokemon.csv", usecols=use_cols, delimiter='\x07')
primary_keys = ["ID"]

dedup_df = df.drop_duplicates(subset=[primary_keys])
# '~' Tilde is a bitwise NOT operator
dedup_df2 = df[~df.index.duplicated('ID')]
# Discard the old index, and create new starting from 0
dedup_df2.reset_index(drop=True)

non_empty_df = dedup_df[pd.isnull(dedup_df.ID)]
for index, row in non_empty_df.iterrows():
    if str(row['Name']) not in ["null", "NULL", "nan"]:
        line = []
        for col in use_cols:
            line.append(row[col])
            line.append(", ")
        print(line)

## selection & indexing
# label-based selection: first row, col 'Name'
print(df.loc[0, 'Name'])
print(df.at[0, 'Name'])  # Optimized for label lookup
# position-based selection: first row, first col
print(df.iloc[0,0])
print(df.iat[0,0])  # Optimized for integer position lookup

# from label 0 to 5 (inclusive) and all columns with labels 'Name' and 'Age'
print(df.loc[0:5, ['Name', 'Age']])

# filtering by query, return a new dataframe
new_df = df.query('Age>18')

## Add new column (feature enigneering), return a new dataframe
new_df2 = new_df.eval('Level = Exp / Age', inplace=False)
# new_df['Level'] = new_df['Exp'] / new_df['Age']

new_df2 = new_df2.assign(Rank = lambda x: x.Level + x.Exp)

## read df as multiple data chunks:
# delimiter='\x7C' ('|');  '\x2C' (','); '\x07' ('^G')
data_chunk = pd.read_csv("dataset_path", header=0, encoding='utf-8', delimiter='\x07', chunksize=10000)

## return first n rows
n = 50
needed_data = df.head(n)


## apply filter to df
condition = ['2021-01-01', '2021-01-03']
filtered_df = df.loc[df['col_date'].isin(condition), ['col_date','col2']]

# drop rows with null value
filtered_df.dropna(subset=['col_date'], inplace=True)

## drop a column
del filtered_df['col2']



# join & merge dfs
left_df = pd.read_csv("df1.csv", delimiter='\x07')
right_df = pd.read_csv("df2.csv", delimiter='\x07')
merged_df = pd.merge(left_df, right_df, how='inner', left_on='left_id', right_on='right_id', suffixes=("", ""))

# dataframe append by row
left_df.append(right_df, ignore_index=True)

dataframe_list = [left_df, right_df]
final_df = pd.concat(dataframe_list, axis=0)

# dataframe append by column
final_df = pd.concat(dataframe_list, axis=1)


# rename a column
final_df.rename(columns={'ts':'pit_timestamp'}, inplace=True)
