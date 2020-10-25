import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Reads in the csv files
acs_df = pd.read_csv('acs_subset_county_level_economic_data.csv')
county_df = pd.read_csv('county_level_data.csv')

# Creates 2 different dataframes, 1 including only total population county measurements, and 1 with only ppl over 60
acs_total_pop = acs_df[acs_df['DESCRIPTION'] == "Total_Estimate"]
acs_over_60 = acs_df[acs_df['DESCRIPTION'] == "Pop_Over_60_Estimate"]

# Selects unwanted column indexes (Everything that is not in Region, County, Population, Sex, Race, Language, Income, Poverty)
unwanted_columns = [0, 4, 8]
for i in range(88):
    if 19 <= i <= 54:
        unwanted_columns.append(i)
    if 59 <= i <= 66:
        unwanted_columns.append(i)
    if 83 <= i <= 87:
        unwanted_columns.append(i)

# Both total pop and over 60 now only include Region, County, Population, Sex, Race, Language, Income, and Poverty
acs_total_pop.drop(acs_total_pop.columns[unwanted_columns], axis=1, inplace=True)
acs_over_60.drop(acs_total_pop.columns[unwanted_columns], axis=1, inplace=True)

# Test plot of Race_White on a histogram
acs_total_pop['RACE_White'].plot(kind='hist')
plt.show()
# Prints data of the total pop acs dataframe
acs_total_pop.info()

# Exports to CSV
# acs_total_pop.to_csv(r'/Users/jefferyshen/Desktop/Stanford Materials:Classes/Datathon\Q6and8_acs_data.csv', index = False)
# acs_over_60.to_csv(r'/Users/jefferyshen/Desktop/Stanford Materials:Classes/Datathon\Q6and8_acs_data_over60.csv', index = False)