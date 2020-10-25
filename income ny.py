import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model
from sklearn.metrics import r2_score


df = pd.read_csv("income.csv")
inc = df.loc[[12, 13, 28, 58, 72, 86, 97, 116, 122]]

x_inc = inc[['mortality_rate']].to_numpy()
y = inc[["INCOME_12_MONTHS_WITH_Social_Security"]].to_numpy()

inc.plot("mortality_rate", "INCOME_12_MONTHS_WITH_Social_Security", kind='scatter')
model = linear_model.LinearRegression()
model.fit(x_inc, y)
#predict = model.predict(x_inc)
plt.plot(x_inc, model.predict(x_inc))
plt.show()
print(model.score(x_inc, y))