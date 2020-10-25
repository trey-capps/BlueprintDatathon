import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv("language.csv")

lang = df.loc[[12, 13, 28, 58, 72, 86, 97, 116, 122]]

x = lang[["mortality_rate"]].to_numpy()
y_eng_ny = lang[["LANGUAGE_English_Only"]].to_numpy()
y_other_ny = lang[["LANGUAGE_Other_Than_ English"]].to_numpy()
y_limit_ny = lang[["LANGUAGE_Limited_English"]].to_numpy()


# english only
lang.plot("mortality_rate", "LANGUAGE_English_Only", kind='scatter')
model = linear_model.LinearRegression()
model.fit(x, y_eng_ny)
predict = model.predict(x)
plt.plot(x, model.predict(x))
plt.show()

print(model.score(x, y_eng_ny))


# other than eng
lang.plot("mortality_rate", "LANGUAGE_Other_Than_ English", kind='scatter')
modelother = linear_model.LinearRegression()
modelother.fit(x, y_other_ny)
predict = modelother.predict(x)
plt.plot(x, modelother.predict(x))
plt.show()

print(modelother.score(x, y_other_ny))


# limited eng
lang.plot("mortality_rate", "LANGUAGE_Limited_English", kind='scatter')
modellimit = linear_model.LinearRegression()
modellimit.fit(x, y_limit_ny)
predict = modellimit.predict(x)
plt.plot(x, modellimit.predict(x))
plt.show()

print(modellimit.score(x, y_limit_ny))

