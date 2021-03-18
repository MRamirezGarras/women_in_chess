import pandas as pd
import os
from plotnine import *

#This file reads the fide ranking files from 2005 to 2021 and shows the proportion of women in ches and the
#mean rating per sex

#FIDE files have 2 different formats. Files with each format are in a different folder
#Read files with old format
old_names = os.listdir("data\old_format")

df_list_number = []#Stores the number of women
df_list_elo = []#Stores the mean rating

for name in old_names:
    year = name[3:5]#Get year from file name
    data = pd.read_fwf(f'data\old_format\{name}', delimiter=' ')
    #Split the data in men and women
    data_w = data.loc[(data.Flag == "w") | (data.Flag == "wi")]
    data_m = data.loc[(data.Flag != "w") & (data.Flag != "wi")]
    #Calculate percentage of men and women
    percent_w = data_w.shape[0] / data.shape[0] *100
    percent_m = 100 - percent_w
    #Calculate the mean rating of men and women
    elo_w = data_w.iloc[:,3 ].mean()
    elo_m = data_m.iloc[:,3 ].mean()
    #Add info to list as dictionary
    df_list_number.append({"year": "20" + str(year), "percent": percent_w, "Sex": "Women"})
    df_list_number.append({"year": "20" + str(year), "percent": percent_m, "Sex": "Men"})
    df_list_elo.append({"year": "20" + str(year), "elo": elo_w, "Sex": "Women"})
    df_list_elo.append({"year": "20" + str(year), "elo": elo_m, "Sex": "Men"})

#Read files with new format
new_names = os.listdir("data\\new_format")

for name in new_names:
    year = pd.to_numeric(name[12:14])#Get year from file name
    if year < 17:#Format changed after 16, adding one column. This selects the right column for ranking
        num = 7
    else:
        num=8
    data = pd.read_fwf(f'data\\new_format\{name}', delimiter=' ')
    data.iloc[:, num] = pd.to_numeric(data.iloc[:, num], errors="coerce")
    #Splits data in men and women
    data_w = data.loc[data.Sex == "F"]
    data_m = data.loc[data.Sex == "M"]
    #Calculate the percentage of men and women
    percent_w = data_w.shape[0] / data.shape[0] * 100
    percent_m = 100 - percent_w
    #Calculate mean rating for men and women
    elo_w = data_w.iloc[:,num].mean()
    elo_m = data_m.iloc[:,num].mean()
    #Append data to a list of dictionaries
    df_list_number.append({"year": "20" + str(year), "percent": percent_w, "Sex": "Women"})
    df_list_number.append({"year": "20" + str(year), "percent": percent_m, "Sex": "Men"})
    df_list_elo.append({"year": "20" + str(year), "elo": elo_w, "Sex": "Women"})
    df_list_elo.append({"year": "20" + str(year), "elo": elo_m, "Sex": "Men"})

#Convert lists of dictionaries into dataframes
df_number = pd.DataFrame(df_list_number, columns= ["year", "percent", "Sex"])
df_elo = pd.DataFrame(df_list_elo, columns= ["year", "elo", "Sex"])

#Convert year into numeric and sort for a better visualization
df_number.year = pd.to_numeric(df_number.year)
df_number = df_number.sort_values("year")
df_elo.year = pd.to_numeric(df_elo.year)
df_elo = df_elo.sort_values("year")

#Plot percentage of women per year
ggplot(df_number[df_number.Sex == "Women"], aes(x="year", y="percent")) + \
    geom_bar(stat="identity", fill = "Blue") + \
    labs(x="Year", y= "Percentage women", title = "Percentage of women in chess") + \
    coord_cartesian(ylim=(0, 12)) + \
    theme_classic()

#Plot mean rating in men and women per year
ggplot(df_elo, aes(x="year", y = "elo", fill="Sex")) + \
    geom_bar(stat="identity", position = "dodge") + \
    labs(x="Year", y="Elo rating", title="Elo rating for men and women") + \
    coord_cartesian(ylim=(1000, 2100) )+ \
    theme_classic() + \
    theme(legend_position = (0.8, 0.8))
