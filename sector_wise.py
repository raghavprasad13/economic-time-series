import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabula import read_pdf

pd.set_option('display.max_colwidth', 75)
pd.set_option('display.max_rows', 200)

df_sector_1993_94_1 = read_pdf("Sector wise 1993-94 1.pdf")
df_sector_1993_94_2 = read_pdf("Sector wise 1993-94 2.pdf")
df_sector_1993_94_3 = read_pdf("Sector wise 1993-94 3.pdf")
# df_sector_1999_2000 = read_pdf("Sector wise 1999-2000.pdf", pages = "all")

# print(df_sector_1993_94_1)
# print()
# print('############################################\n')
# print(df_sector_1993_94_2)
# print()
# print('############################################\n')
# print(df_sector_1993_94_3)
# print()
# print('############################################\n')

col_list_1993_94_1 = df_sector_1993_94_1.columns
col_list_1993_94_2 = df_sector_1993_94_2.columns
col_list_1993_94_3 = df_sector_1993_94_3.columns

# col_list_1999_2000 = df_sector_1999_2000.columns

df_sector_1993_94_1 = df_sector_1993_94_1.loc[4:38, df_sector_1993_94_1.columns.isin([col_list_1993_94_1[0], col_list_1993_94_1[2], col_list_1993_94_1[5]])].set_index(col_list_1993_94_1[0])
df_sector_1993_94_2 = df_sector_1993_94_2.loc[4:38, df_sector_1993_94_2.columns.isin([col_list_1993_94_2[0], col_list_1993_94_2[2], col_list_1993_94_2[3], col_list_1993_94_2[5]])].set_index(col_list_1993_94_2[0])
df_sector_1993_94_3 = df_sector_1993_94_3.loc[5:39, df_sector_1993_94_3.columns.isin([col_list_1993_94_3[0], col_list_1993_94_3[2], col_list_1993_94_3[4]])].set_index(col_list_1993_94_3[0])

# print(df_sector_1993_94_1)
# print()
# print('############################################\n')
# print(df_sector_1993_94_2)
# print()
# print('############################################\n')


df_sector_1993_94_3['Trade, hotels, transport & communication'] = pd.Series([df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]].split(' ')[0] for x in df_sector_1993_94_3.index.tolist()], index=df_sector_1993_94_3.index)
df_sector_1993_94_3['Financing, insurance, real estate & business services'] = pd.Series([df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]].split(' ')[2] for x in df_sector_1993_94_3.index.tolist()], index=df_sector_1993_94_3.index)
df_sector_1993_94_3 = df_sector_1993_94_3.drop(col_list_1993_94_3[2], axis=1)

# for x in df_sector_1993_94_3.index.tolist():

# print(df_sector_1993_94_3)
# print()
# print('############################################\n')

col_list_1993_94_3 = df_sector_1993_94_3.columns


for x in df_sector_1993_94_1.index.tolist():
	df_sector_1993_94_1.loc[x][col_list_1993_94_1[2]] = int(df_sector_1993_94_1.ix[x][col_list_1993_94_1[2]].split(' ')[0])
	df_sector_1993_94_1.loc[x][col_list_1993_94_1[5]] = int(df_sector_1993_94_1.ix[x][col_list_1993_94_1[5]].split(' ')[0])
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[2]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[2]].split(' ')[0])
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[3]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[3]].split(' ')[0])
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[5]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[5]].split(' ')[0])
	df_sector_1993_94_3.loc[x][col_list_1993_94_3[0]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[0]].split(' ')[0])
	df_sector_1993_94_3.loc[x][col_list_1993_94_3[1]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[1]])
	df_sector_1993_94_3.loc[x][col_list_1993_94_3[2]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]])


# df_sector_1993_94_1.apply(pd.to_numeric)

df_sector_1993_94_1['Primary sector'] = pd.Series([(df_sector_1993_94_1.ix[x][col_list_1993_94_1[2]]+df_sector_1993_94_1.ix[x][col_list_1993_94_1[5]]) for x in df_sector_1993_94_1.index.tolist()], index=df_sector_1993_94_1.index)
df_sector_1993_94_2['Secondary sector'] = pd.Series([(df_sector_1993_94_2.ix[x][col_list_1993_94_2[2]]+df_sector_1993_94_2.ix[x][col_list_1993_94_2[3]]+df_sector_1993_94_2.ix[x][col_list_1993_94_2[5]]) for x in df_sector_1993_94_2.index.tolist()], index=df_sector_1993_94_2.index)
df_sector_1993_94_3['Tertiary sector'] = pd.Series([(df_sector_1993_94_3.ix[x][col_list_1993_94_3[0]]+df_sector_1993_94_3.ix[x][col_list_1993_94_3[1]]+df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]]) for x in df_sector_1993_94_3.index.tolist()], index=df_sector_1993_94_3.index)

df

print(df_sector_1993_94_1)
print()
print('########################################################################################\n')
print(df_sector_1993_94_2)
print()
print('########################################################################################\n')
print(df_sector_1993_94_3)
print()
print('########################################################################################\n')







