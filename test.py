import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabula import read_pdf


df_1993_94 = read_pdf("1993-94.pdf")
df_1999_2000 = read_pdf("1999-2000.pdf")
df_2004_05 = read_pdf("2004-05.pdf")
df_2011_12 = read_pdf("2011-12.pdf")


# print(df_1993_94)			# index 6
# print()
# print(df_1999_2000)		# index 6
# print()
# print(df_2004_05)			# index 3
# print()
# print(df_2011_12)
# print()

col_list_1993_94 = df_1993_94.columns
col_list_1999_2000 = df_1999_2000.columns
col_list_2004_05 = df_2004_05.columns
col_list_2011_12 = df_2011_12.columns

# print(col_list_1993_94)
# print()
# print(col_list_1999_2000)
# print()
# print(col_list_2004_05)
# print()

df_1993_94 = df_1993_94.loc[6:, df_1993_94.columns.isin([col_list_1993_94[0], col_list_1993_94[2]])].set_index(col_list_1993_94[0]).apply(pd.to_numeric)
# df_1993_94[col_list_1993_94[2]] = pd.to_numeric(df_1993_94[col_list_1993_94[2]])

df_1999_2000 = df_1999_2000.loc[6:, col_list_1999_2000[0]:col_list_1999_2000[1]].set_index(col_list_1999_2000[0]).apply(pd.to_numeric)
# df_1999_2000[col_list_1999_2000[1]] = pd.to_numeric(df_1999_2000[col_list_1999_2000[1]])

df_2004_05 = df_2004_05.loc[3:, col_list_2004_05[0]:col_list_2004_05[1]].set_index(col_list_2004_05[0]).apply(pd.to_numeric)
# df_2004_05[col_list_2004_05[1]] = pd.to_numeric(df_2004_05[col_list_2004_05[1]])

df_2004_05.loc[:, col_list_2004_05[1]] *= 100
# df_2004_05.loc[:, col_list_2004_05[1]] = int(df_2004_05.loc[:, col_list_2004_05[1]])

const_93_to_99 = df_1999_2000.ix['1999-00'][col_list_1999_2000[1]]/df_1993_94.ix['1999-00'][col_list_1993_94[2]]
const_99_to_93 = df_1993_94.ix['1993-94'][col_list_1993_94[2]]/df_1999_2000.ix['1993-94'][col_list_1999_2000[1]]

const_99_to_04 = df_2004_05.ix['2004-05'][col_list_2004_05[1]]/df_1999_2000.ix['2004-05'][col_list_1999_2000[1]]
const_04_to_99 = df_1999_2000.ix['1999-00'][col_list_1999_2000[1]]/df_2004_05.ix['1999-00'][col_list_2004_05[1]]

const_93_to_04 = df_2004_05.ix['2004-05'][col_list_2004_05[1]]/df_1993_94.ix['2004-05'][col_list_1993_94[2]]
const_04_to_93 = df_1993_94.ix['1993-94'][col_list_1993_94[2]]/df_2004_05.ix['1993-94'][col_list_2004_05[1]]

df_2004_05.loc['1951-52'] = [const_99_to_04 * df_1999_2000.ix['1951-52'][col_list_1999_2000[1]], ]
df_2004_05.loc['1950-51'] = [const_99_to_04 * df_1999_2000.ix['1950-51'][col_list_1999_2000[1]], ]
df_2004_05.sort_index(inplace=True)

df_1999_2000.loc['2009-10'] = [const_04_to_99 * df_2004_05.ix['2009-10'][col_list_2004_05[1]], ]
df_1999_2000.loc['2010-11'] = [const_04_to_99 * df_2004_05.ix['2010-11'][col_list_2004_05[1]], ]
df_1999_2000.loc['2011-12'] = [const_04_to_99 * df_2004_05.ix['2011-12'][col_list_2004_05[1]], ]
df_1999_2000.loc['2012-13'] = [const_04_to_99 * df_2004_05.ix['2012-13'][col_list_2004_05[1]], ]
df_1999_2000.loc['2013-14'] = [const_04_to_99 * df_2004_05.ix['2013-14'][col_list_2004_05[1]], ]

df_1993_94.loc['2005-06'] = [const_04_to_93 * df_2004_05.ix['2005-06'][col_list_2004_05[1]], ]
df_1993_94.loc['2006-07'] = [const_04_to_93 * df_2004_05.ix['2006-07'][col_list_2004_05[1]], ]
df_1993_94.loc['2007-08'] = [const_04_to_93 * df_2004_05.ix['2007-08'][col_list_2004_05[1]], ]
df_1993_94.loc['2008-09'] = [const_04_to_93 * df_2004_05.ix['2008-09'][col_list_2004_05[1]], ]
df_1993_94.loc['2009-10'] = [const_04_to_93 * df_2004_05.ix['2009-10'][col_list_2004_05[1]], ]
df_1993_94.loc['2010-11'] = [const_04_to_93 * df_2004_05.ix['2010-11'][col_list_2004_05[1]], ]
df_1993_94.loc['2011-12'] = [const_04_to_93 * df_2004_05.ix['2011-12'][col_list_2004_05[1]], ]
df_1993_94.loc['2012-13'] = [const_04_to_93 * df_2004_05.ix['2012-13'][col_list_2004_05[1]], ]
df_1993_94.loc['2013-14'] = [const_04_to_93 * df_2004_05.ix['2013-14'][col_list_2004_05[1]], ]

# print(df_1999_2000)
# print()
# print(df_1993_94)
# print()

df_1993_94_growth = pd.DataFrame(index = df_1993_94.index[1:], columns = [col_list_1993_94[2], ])
df_1993_94_growth = df_1993_94_growth.fillna(0)

df_1999_2000_growth = pd.DataFrame(index = df_1999_2000.index[1:], columns = [col_list_1999_2000[1], ])
df_1999_2000_growth = df_1999_2000_growth.fillna(0)

df_2004_05_growth = pd.DataFrame(index = df_2004_05.index[1:], columns = [col_list_2004_05[1], ])
df_2004_05_growth = df_2004_05_growth.fillna(0)

# print(df_1993_94_growth)

for i in range(1, len(df_1993_94.index)):
	# print('df_1993_94_growth.index[i]: ', df_1993_94.index[i])
	# print('Current year: ', df_1993_94.ix[df_1993_94.index[i]][col_list_1993_94[2]])
	# print('Previous year: ', df_1993_94.ix[df_1993_94.index[i-1]][col_list_1993_94[2]])
	# print('############################################\n')
	df_1993_94_growth.loc[df_1993_94.index[i], col_list_1993_94[2]] = 100 * ((df_1993_94.ix[df_1993_94.index[i]][col_list_1993_94[2]] - df_1993_94.ix[df_1993_94.index[i-1]][col_list_1993_94[2]])/df_1993_94.ix[df_1993_94.index[i-1]][col_list_1993_94[2]])
	df_1999_2000_growth.loc[df_1999_2000.index[i], col_list_1999_2000[1]] = 100 * ((df_1999_2000.ix[df_1999_2000.index[i]][col_list_1999_2000[1]] - df_1999_2000.ix[df_1999_2000.index[i-1]][col_list_1999_2000[1]])/df_1999_2000.ix[df_1999_2000.index[i-1]][col_list_1999_2000[1]])
	df_2004_05_growth.loc[df_2004_05.index[i], col_list_2004_05[1]] = 100 * ((df_2004_05.ix[df_2004_05.index[i]][col_list_2004_05[1]] - df_2004_05.ix[df_2004_05.index[i-1]][col_list_2004_05[1]])/df_2004_05.ix[df_2004_05.index[i-1]][col_list_2004_05[1]])

# print(df_1993_94_growth)
# print()
# print(df_1999_2000_growth)
# print()
# print(df_2004_05_growth)

# print(df_2004_05)

# print(const_99_to_04)

# print(df_1993_94)

######################################################################################

# Base year = 1993-94

# df_1993_94.plot()

# x = np.array([i for i in range(len(df_1993_94[col_list_1993_94[2]]))])
# # print(x)

# plt.xticks(x, list(df_1993_94.index))
plt.plot(df_1993_94.index, df_1993_94[col_list_1993_94[2]], 'b-o')
# plt.show()

######################################################################################

# Base year = 1999-2000

# df_1999_2000.plot(color='red')

x = np.array([i for i in range(len(df_1999_2000[col_list_1999_2000[1]]))])
# print(x)

plt.xticks(x, list(df_1999_2000.index))
plt.plot(df_1999_2000.index, df_1999_2000[col_list_1999_2000[1]], 'r-o')
# plt.show()

######################################################################################

# Base year = 2004-05

# df_2004_05.plot(color='green')

# x = np.array([i for i in range(len(df_2004_05[col_list_2004_05[1]]))])
# print(x)

# plt.xticks(x, list(df_2004_05.index))
plt.plot(df_2004_05.index, df_2004_05[col_list_2004_05[1]], 'g-o')

plt.ylabel('GDP (in Rs. crore)')
plt.xlabel('Year')

plt.show()



plt.plot(df_1993_94_growth.index, df_1993_94_growth[col_list_1993_94[2]], 'b-o')
plt.plot(df_1999_2000_growth.index, df_1999_2000_growth[col_list_1999_2000[1]], 'r-o')
plt.plot(df_2004_05_growth.index, df_2004_05_growth[col_list_2004_05[1]], 'g-o')

plt.ylabel('Percentage growth in GDP')
plt.xlabel('Year (from 1951-52 to 2013-14)')

plt.show()


# plt.plot(df_1993_94.index, df_1993_94[col_list_1993_94[0]].values, marker="o", label="1993-94")

# print(df_2004_05)



