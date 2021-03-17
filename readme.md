# Women in chess

Women are severely underrepresented in chess, both in professional and amateur competitions.
Besides, their playing strength, measured by the ELO rating, seems to be
weaker than men's strength.

The objective is to analyze the international ratings of the last 15 years 
to check whether the number of female players has increased or
decreased, the effect these changes have had in the rating and to look for possible
causes for this difference in strength.

The data, stored in the data directory, has been downloaded from https://ratings.fide.com/download.phtml
FIDE had used 2 different formats to store the data in the last 15 years, so the files are
stored in separate directories for "old_format" and "new_format".

## Language and libraries

The analysis has been performed with Python and it requires the libraries os 
(to retrieve file names), pandas (to read and manipulate data) and plotnine 
(to plot the data).

## Files

### evolution_by_year.py

Shows the percentage of women in the total number of players in the last 15 years.
Shows the mean rating for men and women in the last 15 years.

### elo_by_age.py

Calculates the mean rating for men and women for different age groups in different years.

### top_100.py

Percentage of women in the top100 players in the world at different ages.
Percentage of women in the total number of players at different ages.

### women_in_chess.ipynb

Code from evolution_by_year.py and top_100.py in Jupyter notebook format

## Conclusions

The percentage of rated women in chess has duplicated in the last 15 years. However,
the relative strength of men and women seems to have stayed the same. 
The analysis of the percentage of players by age groups shows that the percentage
of female players decreases at older ages, and this trend has not changed in the last years.
The number of women in the top100 players declines drastically at an age of around
20-22 years, which suggests that women are less likely than men to try to pursue a 
professional chess career. 