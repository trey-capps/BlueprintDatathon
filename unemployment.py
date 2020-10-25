import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("employment_by_demographic.csv")

unemployment_rate = df.loc[[5, 12, 18, 24, 30, 37, 43, 49, 55, 62, 69, 75, 81]]

#print(unemployment_rate)

del df['Series Name']

row_white = df.iloc[18]
row_black = df.iloc[43]
row_asian = df.iloc[55]
row_hispanic = df.iloc[75]
row_white.plot(label = "white")
row_black.plot(label = "black")
row_asian.plot(label = "asian")
row_hispanic.plot(label = "hispanic")

plt.ylabel('Unemployment Rate')
plt.title('Unemployment Rates of Different Races, 20 yrs and Over')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()
