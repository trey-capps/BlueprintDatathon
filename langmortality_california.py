import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv("language.csv")

lang = df.loc[[0, 1, 25, 42, 54, 57, 59, 68, 69, 70, 89, 90, 108, 112, 113, 124, ]]


x = lang[["mortality_rate"]].to_numpy()
y_eng_ca = lang[["LANGUAGE_English_Only"]].to_numpy()
y_other_ca = lang[["LANGUAGE_Other_Than_ English"]].to_numpy()
y_limit_ca = lang[["LANGUAGE_Limited_English"]].to_numpy()


# english only
lang.plot("mortality_rate", "LANGUAGE_English_Only", kind='scatter')
model = linear_model.LinearRegression()
model.fit(x, y_eng_ca)
predict = model.predict(x)
plt.plot(x, model.predict(x))
plt.show()

print(model.score(x, y_eng_ca))


# other than eng
lang.plot("mortality_rate", "LANGUAGE_Other_Than_ English", kind='scatter')
modelother = linear_model.LinearRegression()
modelother.fit(x, y_other_ca)
predict = modelother.predict(x)
plt.plot(x, modelother.predict(x))
plt.show()

print(modelother.score(x, y_other_ca))


# limited eng
lang.plot("mortality_rate", "LANGUAGE_Limited_English", kind='scatter')
modellimit = linear_model.LinearRegression()
modellimit.fit(x, y_limit_ca)
predict = modellimit.predict(x)
plt.plot(x, modellimit.predict(x))
plt.show()

print(modellimit.score(x, y_limit_ca))