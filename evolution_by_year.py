import pandas as pd
import scipy.stats as stats
import os
from plotnine import *

old_names = os.listdir("data\old_format")

df_list_number = []
df_list_elo = []

for name in old_names:
    year = name[3:5]
    data = pd.read_fwf(f'data\old_format\{name}', delimiter=' ')
    data_w = data.loc[(data.Flag == "w") | (data.Flag == "wi")]
    data_m = data.loc[(data.Flag != "w") & (data.Flag != "wi")]
    percent_w = data_w.shape[0] / data.shape[0] *100
    percent_m = 100 - percent_w
    elo_w = data_w.iloc[:,3 ].mean()
    elo_m = data_m.iloc[:,3 ].mean()

    df_list_number.append({"year": year, "percent": percent_w, "Sex": "Women"})
    df_list_number.append({"year": year, "percent": percent_m, "Sex": "Men"})
    df_list_elo.append({"year": year, "elo": elo_w, "Sex": "Women"})
    df_list_elo.append({"year": year, "elo": elo_m, "Sex": "Men"})


new_names = os.listdir("data\\new_format")

for name in new_names:
    year = pd.to_numeric(name[12:14])
    if year < 17:
        num = 7
    else:
        num=8
    data = pd.read_fwf(f'data\\new_format\{name}', delimiter=' ')
    data.iloc[:, num] = pd.to_numeric(data.iloc[:, num], errors="coerce")
    data_w = data.loc[data.Sex == "F"]
    data_m = data.loc[data.Sex == "M"]
    percent_w = data_w.shape[0] / data.shape[0] * 100
    percent_m = 100 - percent_w
    elo_w = data_w.iloc[:,num].mean()
    elo_m = data_m.iloc[:,num].mean()

    df_list_number.append({"year": year, "percent": percent_w, "Sex": "Women"})
    df_list_number.append({"year": year, "percent": percent_m, "Sex": "Men"})
    df_list_elo.append({"year": year, "elo": elo_w, "Sex": "Women"})
    df_list_elo.append({"year": year, "elo": elo_m, "Sex": "Men"})


df_number = pd.DataFrame(df_list_number, columns= ["year", "percent", "Sex"])
df_elo = pd.DataFrame(df_list_elo, columns= ["year", "elo", "Sex"])

df_number.year = pd.to_numeric(df_number.year)

df_number = df_number.sort_values("year")

ggplot(df_number[df_number.Sex == "Women"], aes(x="year", y="percent")) + \
    geom_bar(stat="identity", fill = "Blue") + \
    labs(x="Year", y= "Percentage women", title = "Percentage of women in chess") + \
    theme_classic()
