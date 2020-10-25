import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv("sex.csv")

# #over 84
# x = df[["mortality_rate"]].to_numpy()
# sum_column = df["proportion_mover84"] + df["proportion_fmover84"]
# df["proportion_over84"] = sum_column
#
# plt.scatter(x, sum_column, label="proportion_over84")
#
#
# #75-84
# x = df[["mortality_rate"]].to_numpy()
# sum_column = df["proportion_m75to84"] + df["proportion_fm75to84"]
# df["proportion_75to84"] = sum_column
#
# plt.scatter(x, sum_column, label="proportion_75to84")
#
#
# # #65-74
# # m = str("proportion_m65to74")
# # f = str("proportion_fm65to74")
# # x = df[["mortality_rate"]].to_numpy()
# # y_m = df[[m]].to_numpy()
# # y_f = df[[f]].to_numpy()
# #
# # plt.scatter(x, y_m, label=m)
# # plt.scatter(x, y_f, label=f)
# #
# # plt.ylabel('Proportion of Population')
# # plt.xlabel('Mortality Rate')
# # plt.legend()
# # plt.show()
#
# # #55-59
# # m = str("proportion_m55to59")
# # f = str("proportion_fm55to59")
# # x = df[["mortality_rate"]].to_numpy()
# # y_m = df[[m]].to_numpy()
# # y_f = df[[f]].to_numpy()
# #
# # plt.scatter(x, y_m, label=m)
# # plt.scatter(x, y_f, label=f)
# #
# # plt.ylabel('Proportion of Population')
# # plt.xlabel('Mortality Rate')
# # plt.legend()
# # plt.show()
#
#
# #45-54
# x = df[["mortality_rate"]].to_numpy()
# sum_column = df["proportion_m45to54"] + df["proportion_fm45to54"]
# df["proportion_45to54"] = sum_column
#
# plt.scatter(x, sum_column, label="proportion_45to54")
# plt.ylabel('Proportion of Population')
# plt.xlabel('Mortality Rate')
#
# #
# #
# # #proportion_m60to64
# # m = str("proportion_m60to64")
# # f = str("proportion_fm60to64")
# # x = df[["mortality_rate"]].to_numpy()
# # y_m = df[[m]].to_numpy()
# # y_f = df[[f]].to_numpy()
# #
# # plt.scatter(x, y_m, label=m)
# # plt.scatter(x, y_f, label=f)
# #
# # plt.ylabel('Proportion of Population')
# # plt.xlabel('Mortality Rate')
# # plt.legend()
# # plt.show()
# #
# #
# # #30-34
# # m = str("proportion_m30to34")
# # f = str("proportion_fm30to34")
# # x = df[["mortality_rate"]].to_numpy()
# # y_m = df[[m]].to_numpy()
# # y_f = df[[f]].to_numpy()
# #
# # plt.scatter(x, y_m, label=m)
# # plt.scatter(x, y_f, label=f)
# #
# # plt.ylabel('Proportion of Population')
# # plt.xlabel('Mortality Rate')
# # plt.legend()
# # plt.show()
# #
# #
# # #proportion_m5to9
# # m = str("proportion_m5to9")
# # f = str("proportion_fm5to9")
# # x = df[["mortality_rate"]].to_numpy()
# # y_m = df[[m]].to_numpy()
# # y_f = df[[f]].to_numpy()
# #
# # plt.scatter(x, y_m, label=m)
# # plt.scatter(x, y_f, label=f)
# #
# # plt.ylabel('Proportion of Population')
# # plt.xlabel('Mortality Rate')
# # plt.legend()
# # plt.show()
# #
# #
# #proportion_m20to24
# x = df[["mortality_rate"]].to_numpy()
# sum_column = df["proportion_m20to24"] + df["proportion_fm20to24"]
# df["proportion_20to24"] = sum_column
#
# plt.scatter(x, sum_column, label="proportion_20to24")
# #
# #
# # #proportion_m15to19
# # x = df[["mortality_rate"]].to_numpy()
# # sum_column = df["proportion_m15to19"] + df["proportion_fm15to19"]
# # df["proportion_15to19"] = sum_column
# #
# # plt.scatter(x, sum_column, label="proportion_15to19")
#
# plt.ylabel('Proportion of Population')
# plt.xlabel('Mortality Rate')
# plt.legend()
# plt.show()
# #
# #
# # #proportion_m10to14
# # m = str("proportion_m10to14")
# # f = str("proportion_fm10to14")
# # x = df[["mortality_rate"]].to_numpy()
# # y_m = df[[m]].to_numpy()
# # y_f = df[[f]].to_numpy()
# #
# # plt.scatter(x, y_m, label=m)
# # plt.scatter(x, y_f, label=f)
# #
# # plt.ylabel('Proportion of Population')
# # plt.xlabel('Mortality Rate')
# # plt.legend()
# # plt.show()
# #
# #
# # #proportion_mless_5
# # m = str("proportion_mless_5")
# # f = str("proportion_fmless_5")
# # x = df[["mortality_rate"]].to_numpy()
# # y_m = df[[m]].to_numpy()
# # y_f = df[[f]].to_numpy()
# #
# # plt.scatter(x, y_m, label=m)
# # plt.scatter(x, y_f, label=f)
# #
# # plt.ylabel('Proportion of Population')
# # plt.xlabel('Mortality Rate')
# # plt.legend()
# # plt.show()

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
    del state['Key']
    total = state.sum()
    total.name = str("Total " + str(i))
    frame = frame.append(total)

frame["mortality_rate"] = frame["tot_deaths"] / frame["tot_cases"]
frame["aged_over60"] = frame["proportion_mover84"]+frame["proportion_fmover84"]+frame["proportion_m75to84"]+frame["proportion_fm75to84"]+frame["proportion_m65to74"]+frame["proportion_fm65to74"]+frame["proportion_m60to64"]+frame["proportion_fm60to64"]
frame.head()
print(frame)

x = frame[["mortality_rate"]].to_numpy()
y = frame[["aged_over60"]].to_numpy()

# model = linear_model.LinearRegression()
# model.fit(x, y)
# predict = model.predict(x)
# plt.plot(x, model.predict(x))
# plt.show()
#
# print(model.score(x, y))

#45-54

sum_column = frame["proportion_m45to54"] + frame["proportion_fm45to54"]
frame["proportion_45to54"] = sum_column
plt.scatter("mortality_rate", "proportion_45to54")

plt.scatter("mortality_rate", "aged_over60")

plt.show()
