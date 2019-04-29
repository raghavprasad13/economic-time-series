import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabula import read_pdf

df_1980_81 = read_pdf('1980-81 1993-94 Goa.pdf')
df_1999_2000 = read_pdf('1999-2000 Goa.pdf')
df_2004_05 = read_pdf('2004-05 Goa.PDF')

# print(df_2004_05)

col_list_1980_81 = df_1980_81.columns
col_list_1993_94 = col_list_1980_81
col_list_1999_2000 = df_1999_2000.columns
col_list_2004_05 = df_2004_05.columns
# print(col_list_2004_05)

df_1993_94 = df_1980_81.loc[23:34, df_1980_81.columns.isin([col_list_1980_81[0], col_list_1980_81[6]])].set_index(col_list_1980_81[0]).apply(pd.to_numeric)

df_1980_81 = df_1980_81.loc[3:20, df_1980_81.columns.isin([col_list_1980_81[0], col_list_1980_81[6]])].set_index(col_list_1980_81[0]).apply(pd.to_numeric)

df_1999_2000 = df_1999_2000.loc[26:34, df_1999_2000.columns.isin([col_list_1999_2000[0], col_list_1999_2000[5]])].set_index(col_list_1999_2000[0])

df_2004_05 = df_2004_05.loc[29:38, df_2004_05.columns.isin([col_list_2004_05[0], col_list_2004_05[5]])].set_index(col_list_2004_05[0])

df_1999_2000.columns = [col_list_1999_2000[5].split(' ')[0], ]

for x in df_1999_2000.index.tolist():
	df_1999_2000.ix[x]['Goa'] = int(df_1999_2000.ix[x]['Goa'].split(' ')[0])

df_2004_05.columns = [col_list_2004_05[5].split(' ')[0], ]

for x in df_2004_05.index.tolist():
	df_2004_05.ix[x]['Goa'] = float(df_2004_05.ix[x]['Goa'].split(' ')[0]) * 100

# print(df_1980_81)
# print(df_1993_94)
# print(df_1999_2000)
# print(df_2004_05)


const_80_to_93 = df_1993_94.ix['1993-94'][col_list_1993_94[6]]/df_1980_81.ix['1993-94'][col_list_1980_81[6]]
for x in df_1980_81.index.tolist()[0:13]:
	df_1993_94.loc[x] = [const_80_to_93 * df_1980_81.ix[x][col_list_1980_81[6]], ]

df_1993_94.sort_index(inplace = True)
print(df_1993_94)

########################################################################################################################

const_93_to_80 = df_1980_81.ix['1980-81'][col_list_1980_81[6]]/df_1993_94.ix['1980-81'][col_list_1993_94[6]]
for x in df_1993_94.index.tolist()[18:]:
	df_1980_81.loc[x] = [const_93_to_80 * df_1993_94.ix[x][col_list_1993_94[6]], ]

print(df_1980_81)


########################################################################################################################


const_80_to_99 = df_1999_2000.ix['1999-00']['Goa']/df_1980_81.ix['1999-00'][col_list_1980_81[6]]
for x in df_1980_81.index.tolist()[0:13]:
	df_1999_2000.loc[x] = [const_80_to_99 * df_1980_81.ix[x][col_list_1980_81[6]], ]


const_93_to_99 = df_1999_2000.ix['1999-00']['Goa']/df_1993_94.ix['1999-00'][col_list_1993_94[6]]
for x in df_1993_94.index.tolist()[13:19]:
	df_1999_2000.loc[x] = [const_93_to_99 * df_1993_94.ix[x]['Goa'], ]

df_1999_2000.sort_index(inplace = True)
print(df_1999_2000)


########################################################################################################################


const_99_to_93 = df_1993_94.ix['1993-94'][col_list_1993_94[6]]/df_1999_2000.ix['1993-94']['Goa']
for x in df_1999_2000.index.tolist()[25:]:
	df_1993_94.loc[x] = [const_99_to_93 * df_1999_2000.ix[x]['Goa']]

print(df_1993_94)


########################################################################################################################


const_99_to_80 = df_1980_81.ix['1980-81'][col_list_1980_81[6]]/df_1999_2000.ix['1980-81']['Goa']
for x in df_1999_2000.index.tolist()[25:]:
	df_1980_81.loc[x] = [const_99_to_80 * df_1999_2000.ix[x]['Goa']]

print(df_1980_81)



const_80_to_04 = df_2004_05.ix['2004-05']['Goa']/df_1980_81.ix['2004-05']['Goa']
const_93_to_04 = df_2004_05.ix['2004-05']['Goa']/df_1993_94.ix['2004-05']['Goa']
const_99_to_04 = df_2004_05.ix['2004-05']['Goa']/df_1999_2000.ix['2004-05']['Goa']
for x in df_1980_81.index.tolist()[0:13]:
	df_2004_05.loc[x] = [const_80_to_04 * df_1980_81.ix[x]['Goa'], ]

for x in df_1993_94.index.tolist()[13:19]:
	df_2004_05.loc[x] = [const_93_to_04 * df_1993_94.ix[x]['Goa'], ]

for x in df_1999_2000.index.tolist()[19:24]:
	df_2004_05.loc[x] = [const_99_to_04 * df_1999_2000.ix[x]['Goa'], ]

df_2004_05.sort_index(inplace = True)
print("2004-05")
print(df_2004_05)


const_04_to_80 = df_1980_81.ix['1980-81']['Goa']/df_2004_05.ix['1980-81']['Goa']
const_04_to_93 = df_1993_94.ix['1993-94']['Goa']/df_2004_05.ix['1993-94']['Goa']
const_04_to_99 = df_1999_2000.ix['1999-00']['Goa']/df_2004_05.ix['1999-00']['Goa']

for x in df_2004_05.index.tolist()[28:]:
	df_1980_81.loc[x] = [const_04_to_80 * df_2004_05.ix[x]['Goa']]
	df_1993_94.loc[x] = [const_04_to_93 * df_2004_05.ix[x]['Goa']]
	df_1999_2000.loc[x] = [const_04_to_99 * df_2004_05.ix[x]['Goa']]

print(df_1980_81)
print(df_1993_94)
print(df_1999_2000)
print(df_2004_05)




p11 = plt.plot(df_1980_81.index, df_1980_81['Goa'], 'y-o')

p12 = plt.plot(df_1993_94.index, df_1993_94[col_list_1993_94[6]], 'b-o')


x = np.array([i for i in range(len(df_1999_2000['Goa']))])

plt.xticks(x, list(df_1999_2000.index), rotation = 'vertical')
p13 = plt.plot(df_1999_2000.index, df_1999_2000['Goa'], 'r-o')

p14 = plt.plot(df_2004_05.index, df_2004_05['Goa'], 'g-o')

plt.ylabel('SGDP (in Rs. crore)')
plt.xlabel('Year')

plt.legend((p11[0], p12[0], p13[0], p14[0]), ('Base year: 1980-81', 'Base year: 1993-94', 'Base year: 1999-00', 'Base year: 2004-05'))

plt.show()




df_1980_81_growth = pd.DataFrame(index = df_1980_81.index[1:], columns = ['Goa', ])
df_1980_81_growth = df_1980_81_growth.fillna(0)

df_1993_94_growth = pd.DataFrame(index = df_1993_94.index[1:], columns = ['Goa', ])
df_1993_94_growth = df_1993_94_growth.fillna(0)

df_1999_2000_growth = pd.DataFrame(index = df_1999_2000.index[1:], columns = ['Goa', ])
df_1999_2000_growth = df_1999_2000_growth.fillna(0)

df_2004_05_growth = pd.DataFrame(index = df_2004_05.index[1:], columns = ['Goa', ])
df_2004_05_growth = df_2004_05_growth.fillna(0)


for i in range(1, len(df_1980_81.index)):
	df_1980_81_growth.loc[df_1980_81.index[i], 'Goa'] = 100 * ((df_1980_81.ix[df_1980_81.index[i]]['Goa'] - df_1980_81.ix[df_1980_81.index[i-1]]['Goa'])/df_1980_81.ix[df_1980_81.index[i-1]]['Goa'])
	df_1993_94_growth.loc[df_1993_94.index[i], 'Goa'] = 100 * ((df_1993_94.ix[df_1993_94.index[i]]['Goa'] - df_1993_94.ix[df_1993_94.index[i-1]]['Goa'])/df_1993_94.ix[df_1993_94.index[i-1]]['Goa'])
	df_1999_2000_growth.loc[df_1999_2000.index[i], 'Goa'] = 100 * ((df_1999_2000.ix[df_1999_2000.index[i]]['Goa'] - df_1999_2000.ix[df_1999_2000.index[i-1]]['Goa'])/df_1999_2000.ix[df_1999_2000.index[i-1]]['Goa'])
	df_2004_05_growth.loc[df_2004_05.index[i], 'Goa'] = 100 * ((df_2004_05.ix[df_2004_05.index[i]]['Goa'] - df_2004_05.ix[df_2004_05.index[i-1]]['Goa'])/df_2004_05.ix[df_2004_05.index[i-1]]['Goa'])

# print(df_1980_81_growth)
# print(df_1993_94_growth)
# print(df_1999_2000_growth)
# print(df_2004_05_growth)



x = np.array([i for i in range(len(df_1999_2000['Goa'])-1)])

plt.xticks(x, list(df_2004_05_growth.index), rotation = 'vertical')
p21 = plt.plot(df_1980_81_growth.index, df_1980_81_growth['Goa'], 'y-o')
p22 = plt.plot(df_1993_94_growth.index, df_1993_94_growth['Goa'], 'b-o')
p23 = plt.plot(df_1999_2000_growth.index, df_1999_2000_growth['Goa'], 'r-o')
p24 = plt.plot(df_2004_05_growth.index, df_2004_05_growth['Goa'], 'g-o')

plt.ylabel('Percentage growth in SGDP')
plt.xlabel('Year')

plt.legend((p21[0], p22[0], p23[0], p24[0]), ('Base year: 1980-81', 'Base year: 1993-94', 'Base year: 1999-00', 'Base year: 2004-05'))

plt.show()
