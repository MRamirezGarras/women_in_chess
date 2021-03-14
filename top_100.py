import pandas as pd
from plotnine import *

#read data into dataframes
data06 = pd.read_fwf('data\old_format\JUL06FRL.TXT', delimiter=' ')
data06[['games','year']] = data06.GamesBorn.str.split("  ",expand=True,)#Split wrong column
data06["year"] = pd.to_numeric(data06["year"])
data06["games"] = pd.to_numeric(data06["games"])
data06["age"] = 2006 - data06["year"]
data06.dropna(subset=["Jul06"], inplace=True)


data11 = pd.read_fwf('data\old_format\may11frl.txt', delimiter=' ')
data11[['games','year']] = data11.GamesBorn.str.split("  ",expand=True,)#Split wrong column
data11["year"] = pd.to_numeric(data11["year"])
data11["games"] = pd.to_numeric(data11["games"])
data11["age"] = 2011 - data11["year"]
data11.dropna(subset=["May10"], inplace=True)

data16 = pd.read_fwf('data\\new_format\standard_may16frl.TXT', delimiter=' ')
data16.rename(columns={"B-day": "year"}, inplace = True)#Rename B-day column to remove "-"
data16["MAY16"] = pd.to_numeric(data16["MAY16"])
data16["year"] = pd.to_numeric(data16["year"])
data16["age"] = 2016 - data16["year"]

data21 = pd.read_fwf('data\\new_format\standard_mar21frl.TXT', delimiter=' ')
data21 = data21[data21.MAR21 != "M 189"] #Fix a wrong line
data21.rename(columns={"B-day": "year"}, inplace = True)#Rename B-day column to remove "-"
data21["MAR21"] = pd.to_numeric(data21["MAR21"])
data21["year"] = pd.to_numeric(data21["year"])
data21["age"] = 2021 - data21["year"]

#Year 21
data21 = data21[data21.Flag != "i"]
data21 = data21[data21.Flag != "wi"]
ages = list(range(11, 44, 3))
df_list = []

for age in ages:
    data = data21[data21["age"] < age]
    data = data.sort_values("MAR21", ascending=False)
    data = data.head(100)
    percentage = data[data["Sex"] == "F"].shape[0]

    df_list.append({"age": "under " + str(age) , "percentage": percentage, "year": 2021})

#Year 16
data16 = data16[data16.Flag != "i"]
data16 = data16[data16.Flag != "wi"]

for age in ages:
    data = data16[data16["age"] < age]
    data = data.sort_values("MAY16", ascending=False)
    data = data.head(100)
    percentage = data[data["Sex"] == "F"].shape[0]

    df_list.append({"age": "under " + str(age) , "percentage": percentage, "year": 2016})

#Year 11
data11 = data11[data11.Flag != "i"]
data11 = data11[data11.Flag != "wi"]


for age in ages:
    data = data11[data11["age"] < age]
    data = data.sort_values("May10", ascending=False)
    data = data.head(100)
    percentage = data[data["Flag"] == "w"].shape[0]

    df_list.append({"age": "under " + str(age) , "percentage": percentage, "year": 2011})


#Year 06
data06 = data06[data06.Flag != "i"]
data06 = data06[data06.Flag != "wi"]

for age in ages:
    data = data06[data06["age"] < age]
    data = data.sort_values("Jul06", ascending=False)
    data = data.head(100)
    percentage = data[data["Flag"] == "w"].shape[0]

    df_list.append({"age": "under " + str(age) , "percentage": percentage, "year": 2006})

df = pd.DataFrame(df_list, columns= ["age", "percentage", "year"])

ggplot(df[df.year == 2021], aes(x="age", y="percentage")) + \
    geom_bar(stat="identity", fill = "Blue") + \
    labs(x="Age", y= "Percentage women", title = "Percentage of women in top 100 players - 2021") + \
    theme_classic() + \
    theme(axis_text_x=element_text(rotation=45, hjust=1))


ggplot(df, aes(x="age", y="percentage")) + \
    geom_bar(stat="identity", fill = "Blue") + \
    labs(y= "Percentage women", title = "Percentage of women in top 100 players") + \
    theme_classic() + \
    theme(axis_text_x=element_text(rotation=45, hjust=1)) + \
    facet_wrap ("~year")
