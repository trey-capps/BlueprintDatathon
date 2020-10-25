import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

"""
df = pd.read_csv("death_beds_60.csv")

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
    del state['covid_mortality_rate']
    total = state.sum()
    total.name = str("Total " + str(i))
    frame = frame.append(total)

print(frame)
"""

df = pd.read_csv("total_state.csv")

x_m = df[["proportion_mover60"]].to_numpy()
x_f = df[["proportion_fmover60"]].to_numpy()
x_tot = df [["proportion_over60"]].to_numpy()
y_icu = df[["#ICU_beds"]].to_numpy()
y_mort = df[["mortality_rate"]].to_numpy()
state = df[["tot_cases"]].to_numpy()

# total population over 60 to icu beds
df.plot("#ICU_beds", "proportion_over60", kind='scatter')
model = linear_model.LinearRegression()
model.fit(y_icu, x_tot)
predict = model.predict(y_icu)
plt.plot(y_icu, model.predict(y_icu))
plt.show()
print(model.score(y_icu, x_tot))

frame = pd.DataFrame([])
df.plot("tot_cases", "proportion_over60", kind='scatter')
model = linear_model.LinearRegression()
model.fit(state, x_tot)
predict = model.predict(state)
plt.plot(state, model.predict(state))
plt.show()
print(model.score(state, x_tot))

df.plot("mortality_rate", "proportion_over60", kind='scatter')
model = linear_model.LinearRegression()
model.fit(y_mort, x_tot)
predict = model.predict(y_mort)
plt.plot(y_mort, model.predict(y_mort))
plt.show()
print(model.score(y_mort, x_tot))

df.plot("mortality_rate", "proportion_over60", kind='scatter')
model = linear_model.LinearRegression()
model.fit(y_mort, x_tot)
predict = model.predict(y_mort)
plt.plot(y_mort, model.predict(y_mort))
plt.show()
print(model.score(y_mort, x_tot))


#frame = df.corr(method = 'pearson')
#print(frame)
#frame.to_csv(r'C:\Users\GarlicSauce\PycharmProjects\blueprint\correlation_coeff.csv', index = True)