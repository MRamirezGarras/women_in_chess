import pandas as pd

#read data into dataframes
data06 = pd.read_fwf('data\old_format\JUL06FRL.TXT', delimiter=' ')
data06[['games','year']] = data06.GamesBorn.str.split("  ",expand=True,)#Split wrong column
data06["year"] = pd.to_numeric(data06["year"])
data06.dropna(subset=["Jul06"], inplace=True)

data11 = pd.read_fwf('data\old_format\may11frl.txt', delimiter=' ')
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

#Mean by age
#13 years
mean06_w_13 = data06_w.Jul06[data06_w.year > 1992].mean()
mean06_m_13 = data06_m.Jul06[data06_m.year > 1992].mean()

mean11_w_13 = data11_w.May10[data11_w.year > 1997].mean()
mean11_m_13 = data11_m.May10[data11_m.year > 1997].mean()

mean21_w_13 = data21_w.MAR21[data21_w.year > 2007].mean()
mean21_m_13 = data21_m.MAR21[data21_m.year > 2007].mean()


#15 years
mean06_w_15 = data06_w.Jul06[data06_w.year > 1990].mean()
mean06_m_15 = data06_m.Jul06[data06_m.year > 1990].mean()

mean11_w_15 = data11_w.May10[data11_w.year > 1995].mean()
mean11_m_15 = data11_m.May10[data11_m.year > 1995].mean()

mean21_w_15 = data21_w.MAR21[data21_w.year > 2005].mean()
mean21_m_15 = data21_m.MAR21[data21_m.year > 2005].mean()

#Number players by age

#Data06
data06_w[data06_w.year > 1990].shape[0]/data06[data06.year > 1990].shape[0] * 100 #15 years
data06_w[(data06_w.year <= 1990) & (data06_w.year > 1980)].shape[0]/data06[(data06.year <= 1990) & (data06.year > 1980)].shape[0] * 100 #16 to 25
data06_w[(data06_w.year <= 1980) & (data06_w.year > 1970)].shape[0]/data06[(data06.year <= 1980) & (data06.year > 1970)].shape[0] * 100
data06_w[(data06_w.year <= 1970) & (data06_w.year > 1960)].shape[0]/data06[(data06.year <= 1970) & (data06.year > 1960)].shape[0] * 100
data06_w[(data06_w.year <= 1960) & (data06_w.year > 1950)].shape[0]/data06[(data06.year <= 1960) & (data06.year > 1950)].shape[0] * 100
data06_w[(data06_w.year <= 1950) & (data06_w.year > 1940)].shape[0]/data06[(data06.year <= 1950) & (data06.year > 1940)].shape[0] * 100

#Data11
data11_w[data11_w.year > 1995].shape[0]/data11[data11.year > 1995].shape[0] * 100 #15 years
data11_w[(data11_w.year <= 1995) & (data11_w.year > 1985)].shape[0]/data11[(data11.year <= 1995) & (data11.year > 1985)].shape[0] * 100 #16 to 25
data11_w[(data11_w.year <= 1985) & (data11_w.year > 1975)].shape[0]/data11[(data11.year <= 1985) & (data11.year > 1975)].shape[0] * 100
data11_w[(data11_w.year <= 1975) & (data11_w.year > 1965)].shape[0]/data11[(data11.year <= 1975) & (data11.year > 1965)].shape[0] * 100
data11_w[(data11_w.year <= 1965) & (data11_w.year > 1955)].shape[0]/data11[(data11.year <= 1965) & (data11.year > 1955)].shape[0] * 100
data11_w[(data11_w.year <= 1955) & (data11_w.year > 1945)].shape[0]/data11[(data11.year <= 1955) & (data11.year > 1945)].shape[0] * 100

#Data21
data21_w[data21_w.year > 2005].shape[0]/data21[data21.year > 2005].shape[0] * 100 #15 years
data21_w[(data21_w.year <= 2005) & (data21_w.year > 1995)].shape[0]/data21[(data21.year <= 2005) & (data21.year > 1995)].shape[0] * 100 #16 to 25
data21_w[(data21_w.year <= 1995) & (data21_w.year > 1985)].shape[0]/data21[(data21.year <= 1995) & (data21.year > 1985)].shape[0] * 100
data21_w[(data21_w.year <= 1985) & (data21_w.year > 1975)].shape[0]/data21[(data21.year <= 1985) & (data21.year > 1975)].shape[0] * 100
data21_w[(data21_w.year <= 1975) & (data21_w.year > 1965)].shape[0]/data21[(data21.year <= 1975) & (data21.year > 1965)].shape[0] * 100
data21_w[(data21_w.year <= 1965) & (data21_w.year > 1955)].shape[0]/data21[(data21.year <= 1965) & (data21.year > 1955)].shape[0] * 100