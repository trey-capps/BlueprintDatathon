import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model

df = pd.read_csv("age_proportions.csv")

totdeaths = df["tot_deaths"]
totcases = df["tot_cases"]
income = df["INCOME_12_MONTHS_With_Earnings"]
black = df["RACE_Black"]
white = df["RACE_White"]
hispanic = df["RACE_Hispanic_Latino"]
asian = df["RACE_Asian"]
native = df["RACE_American_Indian_Alaska_Native"]
hospital = df["#Hospitals"]
svi = df["SVIPercentile"]
langOther = df["LANGUAGE_Other_Than_ English"]
poverty = df["POVERTY_STATUS_Population"]
demtorep = df["dem_to_rep_ratio"]
population = df["Population"]
mortality = df["mortality_rate"]




minority_sum = hispanic + black + native
df["minority_sum"] = minority_sum

X = df[['POVERTY_STATUS_Population']].to_numpy()
y = df['mortality_rate'].to_numpy()

df.plot("POVERTY_STATUS_Population", "mortality_rate", kind='scatter')
plt.show()

model = linear_model.LinearRegression()
model.fit(X, y)

print(model.coef_, model.intercept_)
print(model.score(X, y))
