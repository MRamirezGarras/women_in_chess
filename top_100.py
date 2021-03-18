import pandas as pd
from plotnine import *

#FIDE used a format to store data until 2012 and a different one from 2013.
#I create functions to read these 2 different formats
#read old format

def read_old_format(name, year, col):
    """Reads a file with the FIDE old format and prepares the datafrade for analysis

        Variables:
        name: name of the file
        year: which year the file belong
        col: name of the column that store the rating
    """
    file = "data\old_format\\" + name
    data = pd.read_fwf(file, delimiter=' ')
    #Number of games and year of birth are incorrectly read in only one column
    #Split the column in 2 and change the type to numeric
    data[['games', 'year']] = data.GamesBorn.str.split("  ", expand=True, )
    data["year"] = pd.to_numeric(data["year"])
    data["games"] = pd.to_numeric(data["games"])
    #Add a new column with the age of the player
    data["age"] = year - data["year"]
    #Remove players without rating
    data.dropna(subset=[col], inplace=True)

    return (data)

#Read data for files from 2006 and 2011
data06 = read_old_format("JUL06FRL.TXT", 2006, "Jul06")
data11 = read_old_format("may11frl.txt", 2011, "May10")

#read new format

def read_new_format(name, year, col):
    """Reads a file with the FIDE new format and prepares the datafrade for analysis
            Variables:
            name: name of the file
            year: which year the file belong
            col: name of the column that store the rating
        """
    file = "data\\new_format\\" + name
    data = pd.read_fwf(file, delimiter=' ')
    #B-day column can cause problems because of "-". Rename and make it numeric
    data.rename(columns={"B-day": "year"}, inplace = True)
    data["year"] = pd.to_numeric(data["year"], errors="coerce")
    data[col] = pd.to_numeric(data[col], errors="coerce")#Make ranking column numeric
    data["age"] = year - data["year"]

    return(data)

#Read data from files from 2016 and 2020
data16 = read_new_format("standard_may16frl.TXT", 2016, "MAY16")
data21 = read_new_format("standard_mar21frl.TXT", 2021, "MAR21")


##Percentage of women in total number of players or top100 players at different ages

df_list_top100 = []#Store data for top100 players
df_list_total = []#Store data for total number of players
ages = list(range(11, 44, 3))

def top100_by_age(df_info, year, col):
    """Calculates the percentage of women in the total number of players or in the top100 players at different ages
        Global variables:
            df_list_top100: list where data for top100 players will be stored
            df_list_total: list where data for total number of players will be stored
            ages: list of ages to calculate the number of women

        Local variables:
            df_info: dataframe that stores the informatio
            year: year where the information was taken
            col: name of the column with the rating
            """
    global ages, df_list
    #Remove inactive players
    data = df_info[df_info.Flag != "i"]
    data = data[data.Flag != "wi"]

    for age in ages:
        data_by_age = data[data["age"] < age]#Select the desired players
        #Create a new dataframe with data from the top 100
        data_top100 = data_by_age.sort_values(col, ascending=False)
        data_top100 = data_top100.head(100)
        #The if clause differentiates between the 2 different formats
        if year > 2012:
            #Calculate the percentage in top100 and in total
            percentage_top100 = data_top100[data_top100["Sex"] == "F"].shape[0]
            percentage_total = data_by_age[data_by_age["Sex"] == "F"].shape[0] / data_by_age.shape[0]
        else:
            percentage_top100 = data_top100[data_top100["Flag"] == "w"].shape[0]
            percentage_total = data_by_age[data_by_age["Flag"] == "w"].shape[0] / data_by_age.shape[0]
        #Append the data to a list of dictionaries
        df_list_top100.append(
            {"age": "under " + str(age), "percentage": percentage_top100, "year": year})
        df_list_total.append(
            {"age": "under " + str(age), "percentage": percentage_total, "year": year})

top100_by_age(data21, 2021, "MAR21")
top100_by_age(data16, 2016, "MAY16")
top100_by_age(data11, 2011, "May10")
top100_by_age(data06, 2006, "Jul06")

#Convert list of dictionaries into dataframes
df_top100 = pd.DataFrame(df_list_top100, columns= ["age", "percentage", "year"])
df_total = pd.DataFrame(df_list_total, columns= ["age", "percentage", "year"])

#Plot data for top100 for 2021
ggplot(df_top100[df_top100.year == 2021], aes(x="age", y="percentage")) + \
    geom_bar(stat="identity", fill = "Blue") + \
    labs(x="Age", y= "Number of women", title = "Number of women in top 100 players - 2021") + \
    theme_classic() + \
    theme(axis_text_x=element_text(rotation=45, hjust=1))

#Plot all data for top100
ggplot(df_top100, aes(x="age", y="percentage")) + \
    geom_bar(stat="identity", fill = "Blue") + \
    labs(y= "Number of women", title = "Number of women in top 100 players") + \
    theme_classic() + \
    theme(axis_text_x=element_text(rotation=45, hjust=1)) + \
    facet_wrap ("~year")


#Plot data for total number of players
ggplot(df_total, aes(x="age", y="percentage")) + \
    geom_bar(stat="identity", fill = "Blue") + \
    labs(y= "Percentage women", title = "Percentage of women in chess") + \
    theme_classic() + \
    theme(axis_text_x=element_text(rotation=45, hjust=1)) + \
    facet_wrap ("~year")