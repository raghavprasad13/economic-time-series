import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabula import read_pdf
from matplotlib.widgets import Button
import time
# import docx

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

# print(col_list_1999_2000_1)

df_sector_1993_94_1 = df_sector_1993_94_1.loc[4:37, df_sector_1993_94_1.columns.isin([col_list_1993_94_1[0], col_list_1993_94_1[2], col_list_1993_94_1[3], col_list_1993_94_1[5]])].set_index(col_list_1993_94_1[0])
df_sector_1993_94_2 = df_sector_1993_94_2.loc[4:38, df_sector_1993_94_2.columns.isin([col_list_1993_94_2[0], col_list_1993_94_2[2], col_list_1993_94_2[3], col_list_1993_94_2[5]])].set_index(col_list_1993_94_2[0])
df_sector_1993_94_3 = df_sector_1993_94_3.loc[5:39, df_sector_1993_94_3.columns.isin([col_list_1993_94_3[0], col_list_1993_94_3[2], col_list_1993_94_3[4]])].set_index(col_list_1993_94_3[0])


df_sector_1999_2000_1 = df_sector_1999_2000_1.loc[4:61, df_sector_1999_2000_1.columns.isin([col_list_1999_2000_1[0], col_list_1999_2000_1[1], col_list_1999_2000_1[2], col_list_1999_2000_1[4]])].set_index(col_list_1999_2000_1[0])
df_sector_1999_2000_2 = df_sector_1999_2000_2.loc[4:61, df_sector_1999_2000_2.columns.isin([col_list_1999_2000_2[0], col_list_1999_2000_2[1], col_list_1999_2000_2[2], col_list_1999_2000_2[4]])].set_index(col_list_1999_2000_2[0])
df_sector_1999_2000_3 = df_sector_1999_2000_3.loc[5:62, df_sector_1999_2000_3.columns.isin([col_list_1999_2000_3[0], col_list_1999_2000_3[1], col_list_1999_2000_3[3]])].set_index(col_list_1999_2000_3[0])

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
	df_sector_1993_94_1.loc[x][col_list_1993_94_1[3]] = int(df_sector_1993_94_1.ix[x][col_list_1993_94_1[3]].split(' ')[0])
	df_sector_1993_94_1.loc[x][col_list_1993_94_1[5]] = int(df_sector_1993_94_1.ix[x][col_list_1993_94_1[5]].split(' ')[0])
	
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[2]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[2]].split(' ')[0])
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[3]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[3]].split(' ')[0])
	df_sector_1993_94_2.loc[x][col_list_1993_94_2[5]] = int(df_sector_1993_94_2.ix[x][col_list_1993_94_2[5]].split(' ')[0])

	df_sector_1993_94_3.loc[x][col_list_1993_94_3[0]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[0]].split(' ')[0])
	df_sector_1993_94_3.loc[x][col_list_1993_94_3[1]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[1]])
	df_sector_1993_94_3.loc[x][col_list_1993_94_3[2]] = int(df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]])


for x in df_sector_1999_2000_1.index.tolist():
	df_sector_1999_2000_1.loc[x][col_list_1999_2000_1[1]] = int(df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[1]].split(' ')[0])
	df_sector_1999_2000_1.loc[x][col_list_1999_2000_1[2]] = int(df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[2]].split(' ')[0])
	df_sector_1999_2000_1.loc[x][col_list_1999_2000_1[4]] = int(df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[4]].split(' ')[0])

	df_sector_1999_2000_2.loc[x][col_list_1999_2000_2[1]] = int(df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[1]].split(' ')[0])
	df_sector_1999_2000_2.loc[x][col_list_1999_2000_2[2]] = int(df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[2]].split(' ')[0])
	df_sector_1999_2000_2.loc[x][col_list_1999_2000_2[4]] = int(df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[4]].split(' ')[0])

	df_sector_1999_2000_3.loc[x][col_list_1999_2000_3[0]] = int(df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[0]].split(' ')[0])
	df_sector_1999_2000_3.loc[x][col_list_1999_2000_3[1]] = int(df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]])
	df_sector_1999_2000_3.loc[x][col_list_1999_2000_3[2]] = int(df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[2]])


const_agri_99_to_93 = df_sector_1993_94_1.ix['1993-94'][col_list_1993_94_1[2]]/df_sector_1999_2000_1.ix['1993-94'][col_list_1999_2000_1[1]]
const_alli_99_to_93 = df_sector_1993_94_1.ix['1993-94'][col_list_1993_94_1[3]]/df_sector_1999_2000_1.ix['1993-94'][col_list_1999_2000_1[2]]
const_mini_99_to_93 = df_sector_1993_94_1.ix['1993-94'][col_list_1993_94_1[5]]/df_sector_1999_2000_1.ix['1993-94'][col_list_1999_2000_1[4]]
const_manu_99_to_93 = df_sector_1993_94_2.ix['1993-94'][col_list_1993_94_2[2]]/df_sector_1999_2000_2.ix['1993-94'][col_list_1999_2000_2[1]]
const_elec_99_to_93 = df_sector_1993_94_2.ix['1993-94'][col_list_1993_94_2[3]]/df_sector_1999_2000_2.ix['1993-94'][col_list_1999_2000_2[2]]
const_cons_99_to_93 = df_sector_1993_94_2.ix['1993-94'][col_list_1993_94_2[5]]/df_sector_1999_2000_2.ix['1993-94'][col_list_1999_2000_2[4]]
const_comm_99_to_93 = df_sector_1993_94_3.ix['1993-94'][col_list_1993_94_3[0]]/df_sector_1999_2000_3.ix['1993-94'][col_list_1999_2000_3[0]]
const_trad_99_to_93 = df_sector_1993_94_3.ix['1993-94'][col_list_1993_94_3[1]]/df_sector_1999_2000_3.ix['1993-94'][col_list_1999_2000_3[1]]
const_fina_99_to_93 = df_sector_1993_94_3.ix['1993-94'][col_list_1993_94_3[2]]/df_sector_1999_2000_3.ix['1993-94'][col_list_1999_2000_3[2]]

# print(df_sector_1999_2000_1.index.tolist()[55:])

for x in df_sector_1999_2000_1.index.tolist()[0:20]:
	df_sector_1993_94_1.loc[x] = [const_agri_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[1]], const_alli_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[2]], const_mini_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[4]]]
	df_sector_1993_94_2.loc[x] = [const_manu_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[1]], const_elec_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[2]], const_cons_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[4]]]
	df_sector_1993_94_3.loc[x] = [const_comm_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[0]], const_trad_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]], const_fina_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[2]]]

df_sector_1993_94_1.sort_index(inplace=True)
df_sector_1993_94_2.sort_index(inplace=True)
df_sector_1993_94_3.sort_index(inplace=True)

for x in df_sector_1999_2000_1.index.tolist()[54:]:
	df_sector_1993_94_1.loc[x] = [const_agri_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[1]], const_alli_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[2]], const_mini_99_to_93 * df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[4]]]
	df_sector_1993_94_2.loc[x] = [const_manu_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[1]], const_elec_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[2]], const_cons_99_to_93 * df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[4]]]
	df_sector_1993_94_3.loc[x] = [const_comm_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[0]], const_trad_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]], const_fina_99_to_93 * df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[2]]]

df_1993_94_all_subsectors = df_sector_1993_94_1

for x in df_sector_1993_94_2.columns:
	df_1993_94_all_subsectors[x] = df_sector_1993_94_2[x]

for x in df_sector_1993_94_3.columns:
	df_1993_94_all_subsectors[x] = df_sector_1993_94_3[x]

# df_1993_94_all_subsectors = df_1993_94_all_subsectors.drop('Primary sector', axis = 1)

df_sector_1993_94_1['Primary sector'] = pd.Series([(df_sector_1993_94_1.ix[x][col_list_1993_94_1[2]]+df_sector_1993_94_1.ix[x][col_list_1993_94_1[5]]) for x in df_sector_1993_94_1.index.tolist()], index=df_sector_1993_94_1.index)
df_sector_1993_94_2['Secondary sector'] = pd.Series([(df_sector_1993_94_2.ix[x][col_list_1993_94_2[2]]+df_sector_1993_94_2.ix[x][col_list_1993_94_2[3]]+df_sector_1993_94_2.ix[x][col_list_1993_94_2[5]]) for x in df_sector_1993_94_2.index.tolist()], index=df_sector_1993_94_2.index)
df_sector_1993_94_3['Tertiary sector'] = pd.Series([(df_sector_1993_94_3.ix[x][col_list_1993_94_3[0]]+df_sector_1993_94_3.ix[x][col_list_1993_94_3[1]]+df_sector_1993_94_3.ix[x][col_list_1993_94_3[2]]) for x in df_sector_1993_94_3.index.tolist()], index=df_sector_1993_94_3.index)

df_sector_1999_2000_1['Primary sector'] = pd.Series([(df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[1]]+df_sector_1999_2000_1.ix[x][col_list_1999_2000_1[4]]) for x in df_sector_1999_2000_1.index.tolist()], index=df_sector_1999_2000_1.index)
df_sector_1999_2000_2['Secondary sector'] = pd.Series([(df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[1]]+df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[2]]+df_sector_1999_2000_2.ix[x][col_list_1999_2000_2[4]]) for x in df_sector_1999_2000_2.index.tolist()], index=df_sector_1999_2000_2.index)
df_sector_1999_2000_3['Tertiary sector'] = pd.Series([(df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[0]]+df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[1]]+df_sector_1999_2000_3.ix[x][col_list_1999_2000_3[2]]) for x in df_sector_1999_2000_3.index.tolist()], index=df_sector_1999_2000_3.index)


df_1993_94 = pd.DataFrame(index = df_sector_1993_94_1.index, columns = None)
df_1999_2000 = pd.DataFrame(index = df_sector_1999_2000_1.index, columns = None)
# df_average = pd.DataFrame(index = df_sector_1993_94_1.index, columns = None)

df_1993_94['Primary sector'] = df_sector_1993_94_1['Primary sector'] 
df_1993_94['Secondary sector'] = df_sector_1993_94_2['Secondary sector']
df_1993_94['Tertiary sector'] = df_sector_1993_94_3['Tertiary sector']

df_1993_94['Total GDP'] = pd.Series([df_1993_94.ix[x]['Primary sector'] + df_1993_94.ix[x]['Secondary sector'] + df_1993_94.ix[x]['Tertiary sector'] for x in df_1993_94.index.tolist()], index = df_1993_94.index)
df_1993_94['% Primary'] = pd.Series([float("{0:.2f}".format(100 * (df_1993_94.ix[x]['Primary sector']/df_1993_94.ix[x]['Total GDP']))) for x in df_1993_94.index.tolist()], index = df_1993_94.index)
df_1993_94['% Secondary'] = pd.Series([float("{0:.2f}".format(100 * (df_1993_94.ix[x]['Secondary sector']/df_1993_94.ix[x]['Total GDP']))) for x in df_1993_94.index.tolist()], index = df_1993_94.index)
df_1993_94['% Tertiary'] = pd.Series([float("{0:.2f}".format(100 * (df_1993_94.ix[x]['Tertiary sector']/df_1993_94.ix[x]['Total GDP']))) for x in df_1993_94.index.tolist()], index = df_1993_94.index)




df_1999_2000['Primary sector'] = df_sector_1999_2000_1['Primary sector'] 
df_1999_2000['Secondary sector'] = df_sector_1999_2000_2['Secondary sector']
df_1999_2000['Tertiary sector'] = df_sector_1999_2000_3['Tertiary sector']



df_growth_1993_94 = pd.DataFrame(index = df_sector_1993_94_1.index[1:], columns = None)
df_growth_1999_2000 = pd.DataFrame(index = df_sector_1999_2000_1.index[1:], columns = None)

for i in range(1, len(df_1993_94)):
	df_growth_1993_94.loc[df_1993_94.index[i], df_1993_94.columns[0]] = 100 * ((df_1993_94.ix[df_1993_94.index[i]][df_1993_94.columns[0]] - df_1993_94.ix[df_1993_94.index[i-1]][df_1993_94.columns[0]])/df_1993_94.ix[df_1993_94.index[i-1]][df_1993_94.columns[0]])
	df_growth_1993_94.loc[df_1993_94.index[i], df_1993_94.columns[1]] = 100 * ((df_1993_94.ix[df_1993_94.index[i]][df_1993_94.columns[1]] - df_1993_94.ix[df_1993_94.index[i-1]][df_1993_94.columns[1]])/df_1993_94.ix[df_1993_94.index[i-1]][df_1993_94.columns[1]])
	df_growth_1993_94.loc[df_1993_94.index[i], df_1993_94.columns[2]] = 100 * ((df_1993_94.ix[df_1993_94.index[i]][df_1993_94.columns[2]] - df_1993_94.ix[df_1993_94.index[i-1]][df_1993_94.columns[2]])/df_1993_94.ix[df_1993_94.index[i-1]][df_1993_94.columns[2]])

	df_growth_1999_2000.loc[df_1999_2000.index[i], df_1999_2000.columns[0]] = 100 * ((df_1999_2000.ix[df_1999_2000.index[i]][df_1999_2000.columns[0]] - df_1999_2000.ix[df_1999_2000.index[i-1]][df_1999_2000.columns[0]])/df_1999_2000.ix[df_1999_2000.index[i-1]][df_1999_2000.columns[0]])
	df_growth_1999_2000.loc[df_1999_2000.index[i], df_1999_2000.columns[1]] = 100 * ((df_1999_2000.ix[df_1999_2000.index[i]][df_1999_2000.columns[1]] - df_1999_2000.ix[df_1999_2000.index[i-1]][df_1999_2000.columns[1]])/df_1999_2000.ix[df_1999_2000.index[i-1]][df_1999_2000.columns[1]])
	df_growth_1999_2000.loc[df_1999_2000.index[i], df_1999_2000.columns[2]] = 100 * ((df_1999_2000.ix[df_1999_2000.index[i]][df_1999_2000.columns[2]] - df_1999_2000.ix[df_1999_2000.index[i-1]][df_1999_2000.columns[2]])/df_1999_2000.ix[df_1999_2000.index[i-1]][df_1999_2000.columns[2]])

df_average_growth = df_growth_1993_94.add(df_growth_1999_2000)
df_average_growth.loc[:] /= 2

# plt.plot(df_average_growth.index, df_average_growth['Primary sector'], 'b-o', label='PS')
# plt.plot(df_average_growth.index, df_average_growth['Secondary sector'], 'r-o', label='SS')
# plt.plot(df_average_growth.index, df_average_growth['Tertiary sector'], 'g-o', label='TS')
# plt.show()

diff_df = df_growth_1999_2000.sub(df_growth_1993_94)


# print(df_1993_94_all_subsectors)
# print()
# print('########################################################################################\n')
# print(df_1993_94_all_subsectors.columns)
# print(df_sector_1993_94_1)
# print()
# print('########################################################################################\n')
# print(df_sector_1993_94_2)
# print()
# print('########################################################################################\n')
print(df_sector_1993_94_3)
print()
print('########################################################################################\n')
# print(df_sector_1999_2000_1)
# print()
# print('########################################################################################\n')
# print(df_sector_1999_2000_2)
# print()
# print('########################################################################################\n')
# print(df_sector_1999_2000_3)
# print()
# print('########################################################################################\n')
# print(df_1993_94)
# print()
# print('########################################################################################\n')
# print(df_1999_2000)
# print()
# print('########################################################################################\n')
# print(df_growth_1993_94)
# print()
# print('########################################################################################\n')
# print(df_growth_1999_2000)
# print()
# print('########################################################################################\n')
# print(df_average_growth)
# print()
# print('########################################################################################\n')
# print(diff_df)
# print()
# print('########################################################################################\n')

# df_growth_1993_94.to_csv('Growth percentage 1993-94.tsv', sep = '\t', encoding = 'utf-8')
# df_growth_1999_2000.to_csv('Growth percentage 1999-2000.tsv', sep = '\t', encoding = 'utf-8')

# df_average_growth.to_csv('Growth percentage average.tsv', sep = '\t', encoding = 'utf-8')

# diff_df.to_csv('Difference.tsv', sep = '\t', encoding = 'utf-8')

# df_1993_94.to_csv('1993-94.tsv', sep = '\t', encoding = 'utf-8')

# doc = docx.Document("./Growth.docx")

# t = doc.add_table(df_growth_1993_94.shape[0]+1, df_growth_1993_94.shape[1])
# t.style = 'TableGrid'

# for j in range(df_growth_1993_94.shape[-1]):
#     t.cell(0,j).text = df_growth_1993_94.columns[j]

# for i in range(df_growth_1993_94.shape[0]):
#     for j in range(df_growth_1993_94.shape[-1]):
#         t.cell(i+1,j).text = str(df_growth_1993_94.values[i,j])

# doc.save("./Growth.docx")

df_sector_1993_94_1['Allied activities'] = pd.Series([df_sector_1993_94_1.ix[x][col_list_1993_94_1[2]] - df_sector_1993_94_1.ix[x][col_list_1993_94_1[3]] for x in df_sector_1993_94_1.index.tolist()], index = df_sector_1993_94_1.index)

plt.plot(df_sector_1993_94_1.index, df_sector_1993_94_1[col_list_1993_94_1[2]], 'r-o', label = 'Agriculture')
plt.plot(df_sector_1993_94_1.index, df_sector_1993_94_1['Allied activities'], 'b-o', label = 'Allied activities')
plt.plot(df_sector_1993_94_1.index, df_sector_1993_94_1[col_list_1993_94_1[5]], 'g-o', label = 'Mining')
x = np.array([i for i in range(len(df_sector_1993_94_1.index.tolist()))])
plt.xticks(x, list(df_sector_1993_94_1.index), rotation = 'vertical')

plt.title('Primary sector (Base year: 1993-94)')

plt.ylabel('Gross Product')
plt.xlabel('Year')
plt.gca().legend(('Agriculture', 'Allied activities', 'Mining'))
plt.show()





plt.plot(df_sector_1993_94_2.index, df_sector_1993_94_2[col_list_1993_94_2[2]], 'r-o', label = 'Manufacturing')
plt.plot(df_sector_1993_94_2.index, df_sector_1993_94_2[col_list_1993_94_2[3]], 'b-o', label = 'Electricity, Gas & Water')
plt.plot(df_sector_1993_94_2.index, df_sector_1993_94_2[col_list_1993_94_2[5]], 'g-o', label = 'Construction')
x = np.array([i for i in range(len(df_sector_1993_94_2.index.tolist()))])
plt.xticks(x, list(df_sector_1993_94_2.index), rotation = 'vertical')

plt.title('Secondary sector (Base year: 1993-94)')

plt.ylabel('Gross Product')
plt.xlabel('Year')
plt.gca().legend(('Manufacturing', 'Electricity, Gas & Water', 'Construction'))
plt.show()




plt.plot(df_sector_1993_94_3.index, df_sector_1993_94_3[col_list_1993_94_3[0]], 'r-o', label = 'Community, social & personal services')
plt.plot(df_sector_1993_94_3.index, df_sector_1993_94_3[col_list_1993_94_3[1]], 'b-o', label = 'Trade, hotels, transport & communication')
plt.plot(df_sector_1993_94_3.index, df_sector_1993_94_3[col_list_1993_94_3[2]], 'g-o', label = 'Financing, insurance, real estate & business services')
x = np.array([i for i in range(len(df_sector_1993_94_3.index.tolist()))])
plt.xticks(x, list(df_sector_1993_94_3.index), rotation = 'vertical')

plt.title('Tertiary sector (Base year: 1993-94)')

plt.ylabel('Gross Product')
plt.xlabel('Year')
plt.gca().legend(('Community, social & personal services', 'Trade, hotels, transport & communication', 'Financing, insurance, real estate & business services'))
plt.show()





plt.plot(df_average_growth.index, df_average_growth['Primary sector'], 'b-o', label='PS')
plt.plot(df_average_growth.index, df_average_growth['Secondary sector'], 'r-o', label='SS')
plt.plot(df_average_growth.index, df_average_growth['Tertiary sector'], 'g-o', label='TS')

z1 = np.polyfit(range(len(df_average_growth.index.tolist())), df_average_growth['Primary sector'], 7)
q1 = np.poly1d(z1)
plt.plot(df_average_growth.index, q1(range(len(df_average_growth.index.tolist()))), 'b--')

z2 = np.polyfit(range(len(df_average_growth.index.tolist())), df_average_growth['Secondary sector'], 7)
q2 = np.poly1d(z2)
plt.plot(df_average_growth.index, q2(range(len(df_average_growth.index.tolist()))), 'r--')

z3 = np.polyfit(range(len(df_average_growth.index.tolist())), df_average_growth['Tertiary sector'], 7)
q3 = np.poly1d(z3)
plt.plot(df_average_growth.index, q3(range(len(df_average_growth.index.tolist()))), 'g--')

x = np.array([i for i in range(len(df_growth_1993_94.index.tolist()))])

plt.xticks(x, list(df_growth_1993_94.index), rotation = 'vertical')

plt.ylabel('Percentage Growth')
plt.xlabel('Year')
plt.gca().legend(('Primary sector', 'Secondary sector', 'Tertiary sector'))
plt.show()


fig = plt.figure()

p1 = plt.bar(df_1993_94.index, df_1993_94['Primary sector'])
# ax = df_1993_94['Primary sector'].plot(kind='bar')
p2 = plt.bar(df_1993_94.index, df_1993_94['Secondary sector'], bottom=df_1993_94['Primary sector'])
p3 = plt.bar(df_1993_94.index, df_1993_94['Tertiary sector'], bottom=df_1993_94['Secondary sector']+df_1993_94['Primary sector'])

primary_rects = p1.patches
secondary_rects = p2.patches
tertiary_rects = p3.patches

primary_percentages = [df_1993_94.ix[x]['% Primary'] for x in df_1993_94.index]
secondary_percentages = [df_1993_94.ix[x]['% Secondary'] for x in df_1993_94.index]
teriary_percentages = [df_1993_94.ix[x]['% Tertiary'] for x in df_1993_94.index]

txt = []
count = 1
for rect1, rect2, rect3, label1, label2, label3 in zip(primary_rects, secondary_rects, tertiary_rects, primary_percentages, secondary_percentages, teriary_percentages):
	if count<33:
		height = rect1.get_height() + rect2.get_height() + rect3.get_height()
		temp = str(label1)+" | "+str(label2)+" | "+str(label3)
		t1 = plt.text(rect1.get_x()+rect1.get_width()/2., 1.1*height, temp, ha='center', va='bottom', rotation = 'vertical', fontsize=6)
		t1.set_visible(False)
		txt.append(t1)
		count += 1

	else:
		height1 = rect1.get_height()
		t1 = plt.text(rect1.get_x()+rect1.get_width()/2., height1/3, label1, ha='center', va='bottom', rotation = 'vertical', fontsize=6)
		t1.set_visible(False)
		txt.append(t1)

		height2 = rect2.get_height()
		t2 = plt.text(rect1.get_x()+rect1.get_width()/2., (height2/6)+ height1, label2, ha='center', va='bottom', rotation = 'vertical', fontsize=6)
		t2.set_visible(False)
		txt.append(t2)

		height3 = rect3.get_height()
		t3 = plt.text(rect1.get_x()+rect1.get_width()/2., height1 + height2 + (height3/5) , label3, ha='center', va='bottom', rotation = 'vertical', fontsize=6)
		t3.set_visible(False)
		txt.append(t3)


def show_percentages(event):
	if event.key != 't':
		return

	for t in txt:
		t.set_visible(not t.get_visible())
		plt.draw()

plt.ylabel('Total GDP (Rs. Crore)')
plt.xlabel('Year')

x = np.array([i for i in range(len(df_1993_94.index.tolist()))])

plt.xticks(x, df_1993_94.index.tolist(), rotation = 'vertical')

plt.legend((p1[0], p2[0], p3[0]), ('Primary Sector', 'Secondary Sector', 'Tertiary Sector'))

plt.connect('key_press_event', show_percentages)

plt.show()

