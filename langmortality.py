import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model

# df = pd.read_csv("language.csv")
#
# x = df[["mortality_rate"]].to_numpy()
# y_eng = df[["LANGUAGE_English_Only"]].to_numpy()
# y_other = df[["LANGUAGE_Other_Than_ English"]].to_numpy()
# y_limit = df[["LANGUAGE_Limited_English"]].to_numpy()
#
#
# # english only
# df.plot("mortality_rate", "LANGUAGE_English_Only", kind='scatter')
# model = linear_model.LinearRegression()
# model.fit(x, y_eng)
# predict = model.predict(x)
# plt.plot(x, model.predict(x))
# plt.show()
#
# print(model.score(x, y_eng))
#
#
# # other than eng
# df.plot("mortality_rate", "LANGUAGE_Other_Than_ English", kind='scatter')
# modelother = linear_model.LinearRegression()
# modelother.fit(x, y_other)
# predict = modelother.predict(x)
# plt.plot(x, modelother.predict(x))
# plt.show()
#
# print(modelother.score(x, y_other))
#
#
# # limited eng
# df.plot("mortality_rate", "LANGUAGE_Limited_English", kind='scatter')
# modellimit = linear_model.LinearRegression()
# modellimit.fit(x, y_limit)
# predict = modellimit.predict(x)
# plt.plot(x, modellimit.predict(x))
# plt.show()
#
# print(modellimit.score(x, y_limit))

df = pd.read_csv("language.csv")

strings = ["Alabama",
           "Arizona",
           "California",
           "Colorado",
           "Connecticut",
           "Delaware",
           "Florida",
           'Georgia',
           'Illinois',
           'Indiana',
           'Kansas',
           'Kentucky',
           'Maryland',
           'Massachusetts',
           'Michigan',
           'Minnesota',
           'Missouri',
           'Nebraska',
           'Nevada',
           'New Jersey',
           'New Mexico',
           'New York',
           'North Carolina',
           'Ohio',
           'Oklahoma',
           'Oregon',
           'Pennsylvania',
           'Rhode Island',
           'South Carolina',
           'Tennessee',
           'Texas',
           'Utah',
           'Washington',
           'Wisconsin']
state = []
frame = pd.DataFrame([])
for i in strings:
    state = df.loc[df["REGION"] == i]
    del state['mortality_rate']
    del state['COUNTY']
    total = state.sum()
    total.name = str("Total " + str(i))
    frame = frame.append(total)

frame["mortality_rate"] = frame["tot_deaths"] / frame["tot_cases"]
frame.head()
print(frame)


x = frame[["mortality_rate"]].to_numpy()
y_eng = frame[["LANGUAGE_English_Only"]].to_numpy()
y_other = frame[["LANGUAGE_Other_Than_ English"]].to_numpy()
y_limit = frame[["LANGUAGE_Limited_English"]].to_numpy()

# english only
frame.plot("mortality_rate", "LANGUAGE_English_Only", kind='scatter')
model = linear_model.LinearRegression()
model.fit(x, y_eng)
predict = model.predict(x)
plt.plot(x, model.predict(x))
plt.show()

print(model.score(x, y_eng))