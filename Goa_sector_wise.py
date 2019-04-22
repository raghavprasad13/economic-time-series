import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabula import read_pdf
from matplotlib.widgets import Button

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df_sector_1993_94 = read_pdf('Goa Sector Wise 1993-94.pdf')
df_sector_1999_2000 = read_pdf('Goa Sector Wise 1999-2000.pdf')

# print(df_sector_1999_2000)

# print(df_sector_1993_94)

col_list_1993_94 = df_sector_1993_94.columns
new_cols = ['Year', ]
for x in col_list_1993_94[1:]:
	new_cols.append(x)

df_sector_1993_94.columns = new_cols

col_list_1993_94 = df_sector_1993_94.columns

# print(col_list_1993_94)

df_sector_1993_94 = df_sector_1993_94.loc[24:35, df_sector_1993_94.columns.isin([col_list_1993_94[0], col_list_1993_94[1], col_list_1993_94[2], col_list_1993_94[3], col_list_1993_94[5], col_list_1993_94[7], col_list_1993_94[8], col_list_1993_94[9], col_list_1993_94[11], col_list_1993_94[12]])].set_index(col_list_1993_94[0])

# print(df_sector_1993_94)

df_sector_1993_94['Agriculture'] = pd.Series([float(df_sector_1993_94.ix[x][col_list_1993_94[1]].split(' ')[0]) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['Allied Activities'] = pd.Series([(float(df_sector_1993_94.ix[x][col_list_1993_94[1]].split(' ')[1]) + float(df_sector_1993_94.ix[x][col_list_1993_94[1]].split(' ')[2])) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['Mining & Quarrying'] = pd.Series([df_sector_1993_94.ix[x][col_list_1993_94[2]] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index).apply(pd.to_numeric)
df_sector_1993_94['Manufacturing'] = pd.Series([float(df_sector_1993_94.ix[x][col_list_1993_94[3]].split(' ')[2]) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['Electricity, Gas & Water supply'] = pd.Series([df_sector_1993_94.ix[x][col_list_1993_94[5]] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index).apply(pd.to_numeric)
df_sector_1993_94['Construction'] = pd.Series([float(df_sector_1993_94.ix[x][col_list_1993_94[7]].split(' ')[0]) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['Trade, hotels, transport & communication'] = pd.Series([float(df_sector_1993_94.ix[x][col_list_1993_94[7]].split(' ')[1]) + float(df_sector_1993_94.ix[x][col_list_1993_94[8]]) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['Financing, insurance, real estate & business services'] = pd.Series([float(df_sector_1993_94.ix[x][col_list_1993_94[9]].split(' ')[0]) + float(df_sector_1993_94.ix[x][col_list_1993_94[9]].split(' ')[1]) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['Community, social & personal services'] = pd.Series([float(df_sector_1993_94.ix[x][col_list_1993_94[11]]) + float(df_sector_1993_94.ix[x][col_list_1993_94[12]]) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)

# print(df_sector_1993_94)

df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[1], axis = 1)
df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[2], axis = 1)
df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[3], axis = 1)
df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[5], axis = 1)
df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[7], axis = 1)
df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[8], axis = 1)
df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[9], axis = 1)
df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[11], axis = 1)
df_sector_1993_94 = df_sector_1993_94.drop(col_list_1993_94[12], axis = 1)

col_list_1993_94 = df_sector_1993_94.columns
print(col_list_1993_94)

# df_sector_1993_94['Primary Sector'] = pd.Series([df_sector_1993_94.ix[x][col_list_1993_94[0]] + df_sector_1993_94.ix[x][col_list_1993_94[1]] + df_sector_1993_94.ix[x][col_list_1993_94[2]] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
# df_sector_1993_94['Secondary Sector'] = pd.Series([df_sector_1993_94.ix[x][col_list_1993_94[3]] + df_sector_1993_94.ix[x][col_list_1993_94[4]] + df_sector_1993_94.ix[x][col_list_1993_94[5]] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
# df_sector_1993_94['Tertiary Sector'] = pd.Series([df_sector_1993_94.ix[x][col_list_1993_94[6]] + df_sector_1993_94.ix[x][col_list_1993_94[7]] + df_sector_1993_94.ix[x][col_list_1993_94[8]] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)






col_list_1999_2000 = df_sector_1999_2000.columns
new_cols = ['Year', ]
for x in col_list_1999_2000[1:]:
	new_cols.append(x)

df_sector_1999_2000.columns = new_cols

col_list_1999_2000 = df_sector_1999_2000.columns

# print(col_list_1999_2000)

df_sector_1999_2000 = df_sector_1999_2000.loc[22:30, df_sector_1999_2000.columns.isin([col_list_1999_2000[0], col_list_1999_2000[1], col_list_1999_2000[2], col_list_1999_2000[3], col_list_1999_2000[5], col_list_1999_2000[7], col_list_1999_2000[8], col_list_1999_2000[9], col_list_1999_2000[11], col_list_1999_2000[12]])].set_index(col_list_1999_2000[0])

# print(df_sector_1999_2000)

df_sector_1999_2000['Agriculture'] = pd.Series([float(df_sector_1999_2000.ix[x][col_list_1999_2000[1]].split(' ')[0]) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['Allied Activities'] = pd.Series([(float(df_sector_1999_2000.ix[x][col_list_1999_2000[1]].split(' ')[1]) + float(df_sector_1999_2000.ix[x][col_list_1999_2000[1]].split(' ')[2])) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['Mining & Quarrying'] = pd.Series([df_sector_1999_2000.ix[x][col_list_1999_2000[2]] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index).apply(pd.to_numeric)
df_sector_1999_2000['Manufacturing'] = pd.Series([float(df_sector_1999_2000.ix[x][col_list_1999_2000[3]].split(' ')[2]) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['Electricity, Gas & Water supply'] = pd.Series([df_sector_1999_2000.ix[x][col_list_1999_2000[5]] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index).apply(pd.to_numeric)
df_sector_1999_2000['Construction'] = pd.Series([float(df_sector_1999_2000.ix[x][col_list_1999_2000[7]].split(' ')[0]) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['Trade, hotels, transport & communication'] = pd.Series([float(df_sector_1999_2000.ix[x][col_list_1999_2000[7]].split(' ')[1]) + float(df_sector_1999_2000.ix[x][col_list_1999_2000[8]]) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['Financing, insurance, real estate & business services'] = pd.Series([float(df_sector_1999_2000.ix[x][col_list_1999_2000[9]].split(' ')[0]) + float(df_sector_1999_2000.ix[x][col_list_1999_2000[9]].split(' ')[1]) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['Community, social & personal services'] = pd.Series([float(df_sector_1999_2000.ix[x][col_list_1999_2000[11]]) + float(df_sector_1999_2000.ix[x][col_list_1999_2000[12]]) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)

# print(df_sector_1999_2000)

df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[1], axis = 1)
df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[2], axis = 1)
df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[3], axis = 1)
df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[5], axis = 1)
df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[7], axis = 1)
df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[8], axis = 1)
df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[9], axis = 1)
df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[11], axis = 1)
df_sector_1999_2000 = df_sector_1999_2000.drop(col_list_1999_2000[12], axis = 1)

col_list_1999_2000 = df_sector_1999_2000.columns
print(col_list_1999_2000)

# df_sector_1999_2000['Primary Sector'] = pd.Series([df_sector_1999_2000.ix[x][col_list_1999_2000[0]] + df_sector_1999_2000.ix[x][col_list_1999_2000[1]] + df_sector_1999_2000.ix[x][col_list_1999_2000[2]] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
# df_sector_1999_2000['Secondary Sector'] = pd.Series([df_sector_1999_2000.ix[x][col_list_1999_2000[3]] + df_sector_1999_2000.ix[x][col_list_1999_2000[4]] + df_sector_1999_2000.ix[x][col_list_1999_2000[5]] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
# df_sector_1999_2000['Tertiary Sector'] = pd.Series([df_sector_1999_2000.ix[x][col_list_1999_2000[6]] + df_sector_1999_2000.ix[x][col_list_1999_2000[7]] + df_sector_1999_2000.ix[x][col_list_1999_2000[8]] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)

# print(df_sector_1993_94)

# print(df_sector_1999_2000)


const_agri_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[0]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[0]]
const_alli_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[1]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[1]]
const_mini_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[2]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[2]]
const_manu_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[3]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[3]]
const_elec_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[4]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[4]]
const_cons_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[5]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[5]]
const_trad_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[6]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[6]]
const_fina_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[7]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[7]]
const_comm_93_to_99 = df_sector_1999_2000.ix['1999-00'][col_list_1999_2000[8]]/df_sector_1993_94.ix['1999-00'][col_list_1993_94[8]]



for x in df_sector_1993_94.index.tolist()[0:6]:
	df_sector_1999_2000.loc[x] = [const_agri_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[0]], 
								const_alli_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[1]], 
								const_mini_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[2]], 
								const_manu_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[3]], 
								const_elec_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[4]], 
								const_cons_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[5]], 
								const_trad_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[6]], 
								const_fina_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[7]], 
								const_comm_93_to_99 * df_sector_1993_94.ix[x][col_list_1993_94[8]]]

df_sector_1999_2000.sort_index(inplace = True)


# print(df_sector_1999_2000)



const_agri_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[0]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[0]]
const_alli_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[1]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[1]]
const_mini_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[2]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[2]]
const_manu_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[3]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[3]]
const_elec_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[4]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[4]]
const_cons_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[5]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[5]]
const_comm_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[6]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[6]]
const_trad_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[7]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[7]]
const_fina_99_to_93 = df_sector_1993_94.ix['1993-94'][col_list_1993_94[8]]/df_sector_1999_2000.ix['1993-94'][col_list_1999_2000[8]]


for x in df_sector_1999_2000.index.tolist()[12:]:
	df_sector_1993_94.loc[x] = [const_agri_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[0]],
								const_alli_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[1]],
								const_mini_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[2]],
								const_manu_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[3]],
								const_elec_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[4]],
								const_cons_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[5]],
								const_trad_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[6]],
								const_fina_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[7]],
								const_comm_99_to_93 * df_sector_1999_2000.ix[x][col_list_1999_2000[8]]]



df_sector_1993_94['Primary Sector'] = pd.Series([df_sector_1993_94.ix[x][col_list_1993_94[0]] + df_sector_1993_94.ix[x][col_list_1993_94[1]] + df_sector_1993_94.ix[x][col_list_1993_94[2]] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['Secondary Sector'] = pd.Series([df_sector_1993_94.ix[x][col_list_1993_94[3]] + df_sector_1993_94.ix[x][col_list_1993_94[4]] + df_sector_1993_94.ix[x][col_list_1993_94[5]] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['Tertiary Sector'] = pd.Series([df_sector_1993_94.ix[x][col_list_1993_94[6]] + df_sector_1993_94.ix[x][col_list_1993_94[7]] + df_sector_1993_94.ix[x][col_list_1993_94[8]] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)


df_sector_1999_2000['Primary Sector'] = pd.Series([df_sector_1999_2000.ix[x][col_list_1999_2000[0]] + df_sector_1999_2000.ix[x][col_list_1999_2000[1]] + df_sector_1999_2000.ix[x][col_list_1999_2000[2]] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['Secondary Sector'] = pd.Series([df_sector_1999_2000.ix[x][col_list_1999_2000[3]] + df_sector_1999_2000.ix[x][col_list_1999_2000[4]] + df_sector_1999_2000.ix[x][col_list_1999_2000[5]] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['Tertiary Sector'] = pd.Series([df_sector_1999_2000.ix[x][col_list_1999_2000[6]] + df_sector_1999_2000.ix[x][col_list_1999_2000[7]] + df_sector_1999_2000.ix[x][col_list_1999_2000[8]] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)


# print(df_sector_1993_94)

# print(df_sector_1999_2000)



df_sector_1993_94['Total GDP'] = pd.Series([df_sector_1993_94.ix[x]['Primary Sector'] + df_sector_1993_94.ix[x]['Secondary Sector'] + df_sector_1993_94.ix[x]['Tertiary Sector'] for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['% Primary'] = pd.Series([float("{0:.2f}".format(100 * (df_sector_1993_94.ix[x]['Primary Sector']/df_sector_1993_94.ix[x]['Total GDP']))) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['% Secondary'] = pd.Series([float("{0:.2f}".format(100 * (df_sector_1993_94.ix[x]['Secondary Sector']/df_sector_1993_94.ix[x]['Total GDP']))) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)
df_sector_1993_94['% Tertiary'] = pd.Series([float("{0:.2f}".format(100 * (df_sector_1993_94.ix[x]['Tertiary Sector']/df_sector_1993_94.ix[x]['Total GDP']))) for x in df_sector_1993_94.index.tolist()], index = df_sector_1993_94.index)



df_sector_1999_2000['Total GDP'] = pd.Series([df_sector_1999_2000.ix[x]['Primary Sector'] + df_sector_1999_2000.ix[x]['Secondary Sector'] + df_sector_1999_2000.ix[x]['Tertiary Sector'] for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['% Primary'] = pd.Series([float("{0:.2f}".format(100 * (df_sector_1999_2000.ix[x]['Primary Sector']/df_sector_1999_2000.ix[x]['Total GDP']))) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['% Secondary'] = pd.Series([float("{0:.2f}".format(100 * (df_sector_1999_2000.ix[x]['Secondary Sector']/df_sector_1999_2000.ix[x]['Total GDP']))) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)
df_sector_1999_2000['% Tertiary'] = pd.Series([float("{0:.2f}".format(100 * (df_sector_1999_2000.ix[x]['Tertiary Sector']/df_sector_1999_2000.ix[x]['Total GDP']))) for x in df_sector_1999_2000.index.tolist()], index = df_sector_1999_2000.index)



print(df_sector_1993_94)
print('##########################################################################################################################################################################\n')
print(df_sector_1999_2000)



df_growth_1993_94 = pd.DataFrame(index = df_sector_1993_94.index[1:], columns = None)
df_growth_1999_2000 = pd.DataFrame(index = df_sector_1999_2000.index[1:], columns = None)

for i in range(1, len(df_sector_1993_94)):
	df_growth_1993_94.loc[df_sector_1993_94.index[i], 'Primary Sector'] = 100 * ((df_sector_1993_94.ix[df_sector_1993_94.index[i]][df_sector_1993_94.columns[0]] - df_sector_1993_94.ix[df_sector_1993_94.index[i-1]][df_sector_1993_94.columns[0]])/df_sector_1993_94.ix[df_sector_1993_94.index[i-1]][df_sector_1993_94.columns[0]])
	df_growth_1993_94.loc[df_sector_1993_94.index[i], 'Secondary Sector'] = 100 * ((df_sector_1993_94.ix[df_sector_1993_94.index[i]][df_sector_1993_94.columns[1]] - df_sector_1993_94.ix[df_sector_1993_94.index[i-1]][df_sector_1993_94.columns[1]])/df_sector_1993_94.ix[df_sector_1993_94.index[i-1]][df_sector_1993_94.columns[1]])
	df_growth_1993_94.loc[df_sector_1993_94.index[i], 'Tertiary Sector'] = 100 * ((df_sector_1993_94.ix[df_sector_1993_94.index[i]][df_sector_1993_94.columns[2]] - df_sector_1993_94.ix[df_sector_1993_94.index[i-1]][df_sector_1993_94.columns[2]])/df_sector_1993_94.ix[df_sector_1993_94.index[i-1]][df_sector_1993_94.columns[2]])

	df_growth_1999_2000.loc[df_sector_1999_2000.index[i], 'Primary Sector'] = 100 * ((df_sector_1999_2000.ix[df_sector_1999_2000.index[i]][df_sector_1999_2000.columns[0]] - df_sector_1999_2000.ix[df_sector_1999_2000.index[i-1]][df_sector_1999_2000.columns[0]])/df_sector_1999_2000.ix[df_sector_1999_2000.index[i-1]][df_sector_1999_2000.columns[0]])
	df_growth_1999_2000.loc[df_sector_1999_2000.index[i], 'Secondary Sector'] = 100 * ((df_sector_1999_2000.ix[df_sector_1999_2000.index[i]][df_sector_1999_2000.columns[1]] - df_sector_1999_2000.ix[df_sector_1999_2000.index[i-1]][df_sector_1999_2000.columns[1]])/df_sector_1999_2000.ix[df_sector_1999_2000.index[i-1]][df_sector_1999_2000.columns[1]])
	df_growth_1999_2000.loc[df_sector_1999_2000.index[i], 'Tertiary Sector'] = 100 * ((df_sector_1999_2000.ix[df_sector_1999_2000.index[i]][df_sector_1999_2000.columns[2]] - df_sector_1999_2000.ix[df_sector_1999_2000.index[i-1]][df_sector_1999_2000.columns[2]])/df_sector_1999_2000.ix[df_sector_1999_2000.index[i-1]][df_sector_1999_2000.columns[2]])


df_average_growth = df_growth_1993_94.add(df_growth_1999_2000)
df_average_growth.loc[:] /= 2

diff_df = df_growth_1999_2000.sub(df_growth_1993_94)

# print(df_growth_1993_94)
# print('##########################################################################################################################################################################\n')
# print(df_growth_1999_2000)
# print('##########################################################################################################################################################################\n')
# print(diff_df)





plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[0]], 'r-o', label = 'Agriculture')
plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[1]], 'b-o', label = 'Allied activities')
plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[2]], 'g-o', label = 'Mining')
x = np.array([i for i in range(len(df_sector_1993_94.index.tolist()))])
plt.xticks(x, list(df_sector_1993_94.index), rotation = 'vertical')

plt.title('Primary sector (Base year: 1993-94)')

plt.ylabel('Gross Product')
plt.xlabel('Year')
plt.gca().legend(('Agriculture', 'Allied activities', 'Mining'))
plt.show()




plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[3]], 'r-o', label = 'Manufacturing')
plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[4]], 'b-o', label = 'Electricity, Gas & Water')
plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[5]], 'g-o', label = 'Construction')
x = np.array([i for i in range(len(df_sector_1993_94.index.tolist()))])
plt.xticks(x, list(df_sector_1993_94.index), rotation = 'vertical')

plt.title('Secondary sector (Base year: 1993-94)')

plt.ylabel('Gross Product')
plt.xlabel('Year')
plt.gca().legend(('Manufacturing', 'Electricity, Gas & Water', 'Construction'))
plt.show()



plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[8]], 'r-o', label = 'Community, social & personal services')
plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[6]], 'b-o', label = 'Trade, hotels, transport & communication')
plt.plot(df_sector_1993_94.index, df_sector_1993_94[col_list_1993_94[7]], 'g-o', label = 'Financing, insurance, real estate & business services')
x = np.array([i for i in range(len(df_sector_1993_94.index.tolist()))])
plt.xticks(x, list(df_sector_1993_94.index), rotation = 'vertical')

plt.title('Tertiary sector (Base year: 1993-94)')

plt.ylabel('Gross Product')
plt.xlabel('Year')
plt.gca().legend(('Community, social & personal services', 'Trade, hotels, transport & communication', 'Financing, insurance, real estate & business services'))
plt.show()





plt.plot(df_average_growth.index, df_average_growth['Primary Sector'], 'b-o', label='PS')
plt.plot(df_average_growth.index, df_average_growth['Secondary Sector'], 'r-o', label='SS')
plt.plot(df_average_growth.index, df_average_growth['Tertiary Sector'], 'g-o', label='TS')

z1 = np.polyfit(range(len(df_average_growth.index.tolist())), df_average_growth['Primary Sector'], 3)
q1 = np.poly1d(z1)
plt.plot(df_average_growth.index, q1(range(len(df_average_growth.index.tolist()))), 'b--')

z2 = np.polyfit(range(len(df_average_growth.index.tolist())), df_average_growth['Secondary Sector'], 3)
q2 = np.poly1d(z2)
plt.plot(df_average_growth.index, q2(range(len(df_average_growth.index.tolist()))), 'r--')

z3 = np.polyfit(range(len(df_average_growth.index.tolist())), df_average_growth['Tertiary Sector'], 3)
q3 = np.poly1d(z3)
plt.plot(df_average_growth.index, q3(range(len(df_average_growth.index.tolist()))), 'g--')

x = np.array([i for i in range(len(df_growth_1993_94.index.tolist()))])

plt.xticks(x, list(df_growth_1993_94.index), rotation = 'vertical')

plt.ylabel('Percentage Growth')
plt.xlabel('Year')
plt.gca().legend(('Primary sector', 'Secondary sector', 'Tertiary sector'))
plt.show()




fig = plt.figure()

p1 = plt.bar(df_sector_1993_94.index, df_sector_1993_94['Primary Sector'])
# ax = df_sector_1993_94['Primary sector'].plot(kind='bar')
p2 = plt.bar(df_sector_1993_94.index, df_sector_1993_94['Secondary Sector'], bottom=df_sector_1993_94['Primary Sector'])
p3 = plt.bar(df_sector_1993_94.index, df_sector_1993_94['Tertiary Sector'], bottom=df_sector_1993_94['Secondary Sector']+df_sector_1993_94['Primary Sector'])

primary_rects = p1.patches
secondary_rects = p2.patches
tertiary_rects = p3.patches

primary_percentages = [df_sector_1993_94.ix[x]['% Primary'] for x in df_sector_1993_94.index]
secondary_percentages = [df_sector_1993_94.ix[x]['% Secondary'] for x in df_sector_1993_94.index]
teriary_percentages = [df_sector_1993_94.ix[x]['% Tertiary'] for x in df_sector_1993_94.index]

txt = []

for rect1, rect2, rect3, label1, label2, label3 in zip(primary_rects, secondary_rects, tertiary_rects, primary_percentages, secondary_percentages, teriary_percentages):
	height1 = rect1.get_height()
	t1 = plt.text(rect1.get_x()+rect1.get_width()/2., height1/3, label1, ha='center', va='bottom', rotation = 'vertical', fontsize=7)
	t1.set_visible(False)
	txt.append(t1)

	height2 = rect2.get_height()
	t2 = plt.text(rect1.get_x()+rect1.get_width()/2., (height2/6)+ height1, label2, ha='center', va='bottom', rotation = 'vertical', fontsize=7)
	t2.set_visible(False)
	txt.append(t2)

	height3 = rect3.get_height()
	t3 = plt.text(rect1.get_x()+rect1.get_width()/2., height1 + height2 + (height3/5) , label3, ha='center', va='bottom', rotation = 'vertical', fontsize=7)
	t3.set_visible(False)
	txt.append(t3)


def show_percentages(event):
	if event.key != 't':
		return

	for t in txt:
		t.set_visible(not t.get_visible())
		plt.draw()


plt.ylabel('Total SGDP (Rs. Crore)')
plt.xlabel('Year')

x = np.array([i for i in range(len(df_sector_1993_94.index.tolist()))])

plt.xticks(x, df_sector_1993_94.index.tolist(), rotation = 'vertical')

plt.legend((p1[0], p2[0], p3[0]), ('Primary Sector', 'Secondary Sector', 'Tertiary Sector'))

plt.connect('key_press_event', show_percentages)

plt.show()



p1 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[0]]/df_sector_1993_94['Total GDP'])
p2 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[1]]/df_sector_1993_94['Total GDP'], bottom = 100*df_sector_1993_94[col_list_1993_94[0]]/df_sector_1993_94['Total GDP'])
p3 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[2]]/df_sector_1993_94['Total GDP'], bottom = (100*df_sector_1993_94[col_list_1993_94[0]]/df_sector_1993_94['Total GDP']) + (100*df_sector_1993_94[col_list_1993_94[1]]/df_sector_1993_94['Total GDP']))


plt.ylabel('% Contribution to Total SGDP')
plt.xlabel('Year')

x = np.array([i for i in range(len(df_sector_1993_94.index.tolist()))])

plt.xticks(x, df_sector_1993_94.index.tolist(), rotation = 'vertical')

plt.legend((p1[0], p2[0], p3[0]), ('Agriculture', 'Allied activities', 'Mining & Quarrying'))

plt.show()






p1 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[3]]/df_sector_1993_94['Total GDP'])
p2 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[4]]/df_sector_1993_94['Total GDP'], bottom = 100*df_sector_1993_94[col_list_1993_94[3]]/df_sector_1993_94['Total GDP'])
p3 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[5]]/df_sector_1993_94['Total GDP'], bottom = (100*df_sector_1993_94[col_list_1993_94[3]]/df_sector_1993_94['Total GDP']) + (100*df_sector_1993_94[col_list_1993_94[4]]/df_sector_1993_94['Total GDP']))


plt.ylabel('% Contribution to Total SGDP')
plt.xlabel('Year')

x = np.array([i for i in range(len(df_sector_1993_94.index.tolist()))])

plt.xticks(x, df_sector_1993_94.index.tolist(), rotation = 'vertical')

plt.legend((p1[0], p2[0], p3[0]), ('Manufacturing', 'Electricity, Gas & Water', 'Construction'))

plt.show()








p1 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[6]]/df_sector_1993_94['Total GDP'])
p2 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[7]]/df_sector_1993_94['Total GDP'], bottom = 100*df_sector_1993_94[col_list_1993_94[6]]/df_sector_1993_94['Total GDP'])
p3 = plt.bar(df_sector_1993_94.index, 100*df_sector_1993_94[col_list_1993_94[8]]/df_sector_1993_94['Total GDP'], bottom = (100*df_sector_1993_94[col_list_1993_94[6]]/df_sector_1993_94['Total GDP']) + (100*df_sector_1993_94[col_list_1993_94[7]]/df_sector_1993_94['Total GDP']))


plt.ylabel('% Contribution to Total SGDP')
plt.xlabel('Year')

x = np.array([i for i in range(len(df_sector_1993_94.index.tolist()))])

plt.xticks(x, df_sector_1993_94.index.tolist(), rotation = 'vertical')

plt.legend((p1[0], p2[0], p3[0]), ('Trade, hotels, transport & communication', 'Financing, insurance, real estate & business services', 'Community, social & personal services'))

plt.show()


