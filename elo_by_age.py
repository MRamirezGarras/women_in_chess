#read data into dataframes
data06 = pd.read_fwf('data\JUL06FRL.TXT', delimiter=' ')
data06[['games','year']] = data06.GamesBorn.str.split("  ",expand=True,)#Split wrong column
data06["year"] = pd.to_numeric(data06["year"])
data06.dropna(subset=["Jul06"], inplace=True)

data11 = pd.read_fwf('data\may11frl.txt', delimiter=' ')
data11[['games','year']] = data11.GamesBorn.str.split("  ",expand=True,)#Split wrong column
data11["year"] = pd.to_numeric(data11["year"])
data11.dropna(subset=["May10"], inplace=True)

data21 = pd.read_fwf('data\\new_format\standard_mar21frl.TXT', delimiter=' ')

data21 = data21[data21.MAR21 != "M 189"] #Fix a wrong line
data21.rename(columns={"B-day": "year"}, inplace = True)#Rename B-day column to remove "-"
data21["MAR21"] = pd.to_numeric(data21["MAR21"])
data21["year"] = pd.to_numeric(data21["year"])


#split data in men and women

data06_w = data06.loc[(data06.Flag == "w") | (data06.Flag == "wi")]
data06_m = data06.loc[(data06.Flag != "w") & (data06.Flag != "wi")]

data11_w = data11.loc[(data11.Flag == "w") | (data11.Flag == "wi")]
data11_m = data11.loc[(data11.Flag != "w") & (data11.Flag != "wi")]

data21_w = data21.loc[data21.Sex == "F"]
data21_m = data21.loc[data21.Sex == "M"]

#Proportion men/woman

print("Proportion women 2006:", round(data06_w.shape[0]/data06.shape[0], 4) * 100, "%")
print("Proportion women 2011:", round(data11_w.shape[0]/data11.shape[0], 4) * 100, "%")
print("Proportion women 2021:", round(data21_w.shape[0]/data21.shape[0], 4) * 100, "%")

#Mean comparisons 21
data21_w.MAR21.mean()
data21_m.MAR21.mean()
stats.ttest_ind(data21_w.MAR21, data21_m.MAR21)
print("Difference ELO 2021: ", data21_w.MAR21.mean() - data21_m.MAR21.mean())

data21_w.MAR21[data21_w.year > 2000].mean()
data21_m.MAR21[data21_m.year > 2000].mean()
stats.ttest_ind(data21_w.MAR21[data21_w.year > 2000], data21_m.MAR21[data21_m.year > 2000])
print("Difference ELO 2021 - young people: ", data21_w.MAR21[data21_w.year > 2000].mean() - data21_m.MAR21[data21_m.year > 2000].mean())


#Mean comparisions 11
data11_w.May10.mean()
data11_m.May10.mean()
stats.ttest_ind(data11_w.May10, data11_m.May10)
print("Difference ELO 2011: ", data11_w.May10.mean() - data11_m.May10.mean())


data11_w.May10[data11_w.year > 1995].mean()
data11_m.May10[data11_m.year > 1995].mean()
stats.ttest_ind(data11_w.May10[data11_w.year > 1995], data11_m.May10[data11_m.year > 1995])
print("Difference ELO 2011 - young people: ", data11_w.May10[data11_w.year > 1995].mean() - data11_m.May10[data11_m.year > 1995].mean())



#Mean comparisions 06
data06_w.Jul06.mean()
data06_m.Jul06.mean()
stats.ttest_ind(data06_w.Jul06, data06_m.Jul06)
print("Difference ELO 2006: ", data06_w.Jul06.mean() - data06_m.Jul06.mean())

data06_w.Jul06[data06_w.year > 1985].mean()
data06_m.Jul06[data06_m.year > 1985].mean()
stats.ttest_ind(data06_w.Jul06[data06_w.year > 1985], data06_m.Jul06[data06_m.year > 1985])

print("Difference ELO 2006 - young people: ", data06_w.Jul06[data06_w.year > 1985].mean() - data06_m.Jul06[data06_m.year > 1985].mean())
