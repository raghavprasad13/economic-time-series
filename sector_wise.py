import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabula import read_pdf

pd.set_option('display.max_colwidth', 75)
pd.set_option('display.max_rows', 200)

df_sector_1993_94_1 = read_pdf("Sector wise 1993-94 1.pdf")
df_sector_1993_94_2 = read_pdf("Sector wise 1993-94 2.pdf")
df_sector_1993_94_3 = read_pdf("Sector wise 1993-94 3.pdf")

df_sector_1999_2000_1 = read_pdf("Sector wise 1999-2000 1.pdf")
df_sector_1999_2000_2 = read_pdf("Sector wise 1999-2000 2.pdf")
df_sector_1999_2000_3 = read_pdf("Sector wise 1999-2000 3.pdf")

# print(df_sector_1999_2000_1)
# print()
# print('############################################\n')
# print(df_sector_1999_2000_2)
# print()
# print('############################################\n')
# print(df_sector_1999_2000_3)
# print()
# print('############################################\n')

col_list_1993_94_1 = df_sector_1993_94_1.columns
col_list_1993_94_2 = df_sector_1993_94_2.columns
col_list_1993_94_3 = df_sector_1993_94_3.columns

col_list_1999_2000_1 = df_sector_1999_2000_1.columns
col_list_1999_2000_2 = df_sector_1999_2000_2.columns
col_list_1999_2000_3 = df_sector_1999_2000_3.columns


df_sector_1993_94_1 = df_sector_1993_94_1.loc[4:38, df_sector_1993_94_1.columns.isin([col_list_1993_94_1[0], col_list_1993_94_1[2], col_list_1993_94_1[5]])].set_index(col_list_1993_94_1[0])
df_sector_1993_94_2 = df_sector_1993_94_2.loc[4:38, df_sector_1993_94_2.columns.isin([col_list_1993_94_2[0], col_list_1993_94_2[2], col_list_1993_94_2[3], col_list_1993_94_2[5]])].set_index(col_list_1993_94_2[0])
df_sector_1993_94_3 = df_sector_1993_94_3.loc[5:39, df_sector_1993_94_3.columns.isin([col_list_1993_94_3[0], col_list_1993_94_3[2], col_list_1993_94_3[4]])].set_index(col_list_1993_94_3[0])


df_sector_1999_2000_1 = df_sector_1999_2000_1.loc[4:62, df_sector_1999_2000_1.columns.isin([col_list_1999_2000_1[0], col_list_1999_2000_1[1], col_list_1999_2000_1[4]])].set_index(col_list_1999_2000_1[0])
df_sector_1999_2000_2 = df_sector_1999_2000_2.loc[4:62, df_sector_1999_2000_2.columns.isin([col_list_1999_2000_2[0], col_list_1999_2000_2[1], col_list_1999_2000_2[2], col_list_1999_2000_2[4]])].set_index(col_list_1999_2000_2[0])
df_sector_1999_2000_3 = df_sector_1999_2000_3.loc[5:63, df_sector_1999_2000_3.columns.isin([col_list_1999_2000_3[0], col_list_1999_2000_3[1], col_list_1999_2000_3[3]])].set_index(col_list_1999_2000_3[0])

# print(df_sector_1999_2000_1)
# print()
# print('############################################\n')
# print(df_sector_1999_2000_2)
# print()
# print('############################################\n')


df_sector_1993_94_3['Trade, hotels, transport & communication'] = pd.Series([df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]].split(' ')[0] for x in df_sector_1993_94_3.index.tolist()], index=df_sector_1993_94_3.index)
df_sector_1993_94_3['Financing, insurance, real estate & business services'] = pd.Series([df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]].split(' ')[2] for x in df_sector_1993_94_3.index.tolist()], index=df_sector_1993_94_3.index)
df_sector_1993_94_3 = df_sector_1993_94_3.drop(col_list_1993_94_3[2], axis=1)

df_sector_1999_2000_3['Trade, hotels, transport & communication'] = pd.Series([df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]].split(' ')[0] for x in df_sector_1999_2000_3.index.tolist()], index=df_sector_1999_2000_3.index)
df_sector_1999_2000_3['Financing, insurance, real estate & business services'] = pd.Series([df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]].split(' ')[2] for x in df_sector_1999_2000_3.index.tolist()], index=df_sector_1999_2000_3.index)
df_sector_1999_2000_3 = df_sector_1999_2000_3.drop(col_list_1999_2000_3[1], axis=1)


# print(df_sector_1999_2000_3)
# print()
# print('############################################\n')

col_list_1993_94_3 = df_sector_1993_94_3.columns

col_list_1999_2000_3 = df_sector_1999_2000_3.columns


for x in df_sector_1993_94_1.index.tolist():
	df_sector_1993_94_1.loc[x][col_list_1993_94_1[2]] = int(df_sector_1993_94_1.ix[x][col_list_1993_94_1[2]].split(' ')[0])
	df_sector_1993_94_1.loc[x][col_list_1993_94_1[5]] = int(df_sector_1993_94_1.ix[x][col_list_1993_94_1[5]].split(' ')[0])
	
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[2]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[2]].split(' ')[0])
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[3]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[3]].split(' ')[0])
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[5]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[5]].split(' ')[0])

	df_sector_1993_94_3.loc[x][col_list_1993_94_3[0]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[0]].split(' ')[0])
	df_sector_1993_94_3.loc[x][col_list_1993_94_3[1]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[1]])
	df_sector_1993_94_3.loc[x][col_list_1993_94_3[2]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]])


for x in df_sector_1999_2000_1.index.tolist():
	df_sector_1999_2000_1.loc[x][col_list_1999_2000_1[1]] = int(df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[1]].split(' ')[0])
	df_sector_1999_2000_1.loc[x][col_list_1999_2000_1[4]] = int(df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[4]].split(' ')[0])

	df_sector_1999_2000_2.loc[x][col_list_1999_2000_2[1]] = int(df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[1]].split(' ')[0])
	df_sector_1999_2000_2.loc[x][col_list_1999_2000_2[2]] = int(df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[2]].split(' ')[0])
	df_sector_1999_2000_2.loc[x][col_list_1999_2000_2[4]] = int(df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[4]].split(' ')[0])

	df_sector_1999_2000_3.loc[x][col_list_1999_2000_3[0]] = int(df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[0]].split(' ')[0])
	df_sector_1999_2000_3.loc[x][col_list_1999_2000_3[1]] = int(df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]])
	df_sector_1999_2000_3.loc[x][col_list_1999_2000_3[2]] = int(df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[2]])


const_agri_99_to_93 = df_sector_1993_94_1.ix['1993-94'][col_list_1993_94_1[2]]/df_sector_1999_2000_1.ix['1993-94'][col_list_1999_2000_1[1]]
const_mini_99_to_93 = df_sector_1993_94_1.ix['1993-94'][col_list_1993_94_1[5]]/df_sector_1999_2000_1.ix['1993-94'][col_list_1999_2000_1[4]]
const_manu_99_to_93 = df_sector_1993_94_2.ix['1993-94'][col_list_1993_94_2[2]]/df_sector_1999_2000_2.ix['1993-94'][col_list_1999_2000_2[1]]
const_elec_99_to_93 = df_sector_1993_94_2.ix['1993-94'][col_list_1993_94_2[3]]/df_sector_1999_2000_2.ix['1993-94'][col_list_1999_2000_2[2]]
const_cons_99_to_93 = df_sector_1993_94_2.ix['1993-94'][col_list_1993_94_2[5]]/df_sector_1999_2000_2.ix['1993-94'][col_list_1999_2000_2[4]]
const_comm_99_to_93 = df_sector_1993_94_3.ix['1993-94'][col_list_1993_94_3[0]]/df_sector_1999_2000_3.ix['1993-94'][col_list_1999_2000_3[0]]
const_trad_99_to_93 = df_sector_1993_94_3.ix['1993-94'][col_list_1993_94_3[1]]/df_sector_1999_2000_3.ix['1993-94'][col_list_1999_2000_3[1]]
const_fina_99_to_93 = df_sector_1993_94_3.ix['1993-94'][col_list_1993_94_3[2]]/df_sector_1999_2000_3.ix['1993-94'][col_list_1999_2000_3[2]]

# print(df_sector_1999_2000_1.index.tolist()[55:])

for x in df_sector_1999_2000_1.index.tolist()[0:20]:
	df_sector_1993_94_1.loc[x] = [const_agri_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[1]], const_mini_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[4]]]
	df_sector_1993_94_2.loc[x] = [const_manu_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[1]], const_elec_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[2]], const_cons_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[4]]]
	df_sector_1993_94_3.loc[x] = [const_comm_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[0]], const_trad_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]], const_fina_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[2]]]

df_sector_1993_94_1.sort_index(inplace=True)
df_sector_1993_94_2.sort_index(inplace=True)
df_sector_1993_94_3.sort_index(inplace=True)

for x in df_sector_1999_2000_1.index.tolist()[55:]:
	df_sector_1993_94_1.loc[x] = [const_agri_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[1]], const_mini_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[4]]]
	df_sector_1993_94_2.loc[x] = [const_manu_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[1]], const_elec_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[2]], const_cons_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[4]]]
	df_sector_1993_94_3.loc[x] = [const_comm_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[0]], const_trad_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]], const_fina_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[2]]]



df_sector_1993_94_1['Primary sector'] = pd.Series([(df_sector_1993_94_1.ix[x][col_list_1993_94_1[2]]+df_sector_1993_94_1.ix[x][col_list_1993_94_1[5]]) for x in df_sector_1993_94_1.index.tolist()], index=df_sector_1993_94_1.index)
df_sector_1993_94_2['Secondary sector'] = pd.Series([(df_sector_1993_94_2.ix[x][col_list_1993_94_2[2]]+df_sector_1993_94_2.ix[x][col_list_1993_94_2[3]]+df_sector_1993_94_2.ix[x][col_list_1993_94_2[5]]) for x in df_sector_1993_94_2.index.tolist()], index=df_sector_1993_94_2.index)
df_sector_1993_94_3['Tertiary sector'] = pd.Series([(df_sector_1993_94_3.ix[x][col_list_1993_94_3[0]]+df_sector_1993_94_3.ix[x][col_list_1993_94_3[1]]+df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]]) for x in df_sector_1993_94_3.index.tolist()], index=df_sector_1993_94_3.index)

df_sector_1999_2000_1['Primary sector'] = pd.Series([(df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[1]]+df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[4]]) for x in df_sector_1999_2000_1.index.tolist()], index=df_sector_1999_2000_1.index)
df_sector_1999_2000_2['Secondary sector'] = pd.Series([(df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[1]]+df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[2]]+df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[4]]) for x in df_sector_1999_2000_2.index.tolist()], index=df_sector_1999_2000_2.index)
df_sector_1999_2000_3['Tertiary sector'] = pd.Series([(df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[0]]+df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]]+df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[2]]) for x in df_sector_1999_2000_3.index.tolist()], index=df_sector_1999_2000_3.index)


df_1993_94 = pd.DataFrame(index = df_sector_1993_94_1.index, columns = None)
df_1999_2000 = pd.DataFrame(index = df_sector_1999_2000_1.index, columns = None)

df_1993_94['Primary sector'] = df_sector_1993_94_1['Primary sector'] 
df_1993_94['Secondary sector'] = df_sector_1993_94_2['Secondary sector']
df_1993_94['Tertiary sector'] = df_sector_1993_94_3['Tertiary sector']

df_1999_2000['Primary sector'] = df_sector_1999_2000_1['Primary sector'] 
df_1999_2000['Secondary sector'] = df_sector_1999_2000_2['Secondary sector']
df_1999_2000['Tertiary sector'] = df_sector_1999_2000_3['Tertiary sector']


print(df_sector_1993_94_1)
print()
print('########################################################################################\n')
print(df_sector_1993_94_2)
print()
print('########################################################################################\n')
print(df_sector_1993_94_3)
print()
print('########################################################################################\n')
print(df_1993_94)
print()
print('########################################################################################\n')

print(df_sector_1999_2000_1)
print()
print('########################################################################################\n')
print(df_sector_1999_2000_2)
print()
print('########################################################################################\n')
print(df_sector_1999_2000_3)
print()
print('########################################################################################\n')
print(df_1999_2000)
print()
print('########################################################################################\n')






