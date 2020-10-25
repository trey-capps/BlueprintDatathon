import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Provisional_Death_Counts_for_Coronavirus_Disease__COVID-19___Distribution_of_Deaths_by_Race_and_Hispanic_Origin (1).csv")

white = df["Non-Hispanic White"]
black = df["Non-Hispanic Black or African American"]
asian = df["Non-Hispanic Asian"]
hispanic = df["Hispanic or Latino"]
native = df["Non-Hispanic American Indian or Alaska Native"]
other = df["Other"]

Unweighted = [60.1, 12.5, 0.7, 5.8, 18.5, 2.4]
Covid = [51.6, 20.5, 1, 4.1, 21.2, 1.5]
index = ['White', 'Black', 'Native American',
         'Asian', 'Hispanic', 'Other']

df = pd.DataFrame({'Percent Distribution of Population': Unweighted,
                   'Percent Distribution Covid Deaths': Covid}, index=index)



ax = df.plot.bar(rot=0)
plt.show()
