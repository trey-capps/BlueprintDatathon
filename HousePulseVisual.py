import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
deny = pd.read_csv('denied_access.csv')

data = deny.copy()
data.drop(labels = 'Quartile Range', inplace = True, axis = 1)
data.dropna(inplace = True)
data.to_csv('access_deny.csv')

cln_data = data.copy()
cln_data.drop(labels = ['Phase', 'Confidence Interval'], inplace = True, axis = 1)

index = list(cln_data['Subgroup'].value_counts().index)
counts = list(cln_data['Subgroup'].value_counts())
group_count = dict(zip(index, counts))
print(group_count)

group_data = data[data['Group'] == 'By State']
st_ind = list(group_data['State'].value_counts().index)
st_cnt = list(group_data['State'].value_counts())
group_count = dict(zip(st_ind, st_cnt))
print(group_count)

dng_data = pd.read_csv('delayed_and_didnot_get_care.csv')

x = dng_data['Value']
age = dng_data[dng_data['Group'] == 'By Age']
nat_est = dng_data[dng_data['Group'] == 'National Estimate']
ethn = dng_data[dng_data['Group'] == 'By Race/Hispanic ethnicity']
state = dng_data[dng_data['Group'] == 'By State']
gend = dng_data[dng_data['Group'] == 'By Gender']
edu = dng_data[dng_data['Group'] == 'By Education']


age18 = age[age['Subgroup'] == '18 - 29 years']
age30 = age[age['Subgroup'] == '30 - 39 years']
age40 = age[age['Subgroup'] == '40 - 49 years']
age50 = age[age['Subgroup'] == '50 - 59 years']
age60 = age[age['Subgroup'] == '60 - 69 years']
age70 = age[age['Subgroup'] == '70 - 79 years']
age80 = age[age['Subgroup'] == '80 years and above']


plt.plot(age18['Week'], age18['Value'], marker='', color='c', linewidth=1, label='18-29')
plt.plot(age30['Week'], age30['Value'], marker='', color='g', linewidth=1, label = '30-39')
plt.plot(age40['Week'], age40['Value'], marker='', color='r', linewidth=1, linestyle='dashed', label='40-49')
plt.plot(age50['Week'], age50['Value'], marker='', color='r', linewidth=1, label='50-59')
plt.plot(age60['Week'], age60['Value'], marker='', color='b', linewidth=1, linestyle='dashed', label='60-69')
plt.plot(age70['Week'], age70['Value'], marker='', color='b', linewidth=1, label='70-79')
plt.plot(age80['Week'], age80['Value'], marker='', color='c', linewidth=1, linestyle='dashed', label='Over 80')
plt.plot(nat_est['Week'], nat_est['Value'], 'k-', linewidth=2, label='National Estimate')
plt.xlabel('Week')
plt.ylabel('Percent denied or did not recieve')
plt.legend(bbox_to_anchor=(1, 1))
plt.show()


male = gend[gend['Subgroup'] == 'Male']
female = gend[gend['Subgroup'] == 'Female']

plt.plot(male['Week'], male['Value'], 'b-', linewidth=2, label='Male')
plt.plot(female['Week'], female['Value'], 'r-', linewidth=2, label = 'Female')
plt.plot(nat_est['Week'], nat_est['Value'], 'k-', linewidth=3, label='National Estimate')
plt.xlabel('Week')
plt.ylabel('Percent denied or did not recieve')
plt.legend()
plt.show()


hisp = ethn[ethn['Subgroup'] == 'Hispanic or Latino']
whit = ethn[ethn['Subgroup'] == 'Non-Hispanic white, single race']
blck = ethn[ethn['Subgroup'] == 'Non-Hispanic black, single race']
asia = ethn[ethn['Subgroup'] == 'Non-Hispanic Asian, single race']
oth = ethn[ethn['Subgroup'] == 'Non-Hispanic, other races and multiple races']


plt.plot(hisp['Week'], hisp['Value'], 'b-', label='Hispanic or Latino')
plt.plot(whit['Week'], whit['Value'], 'g-', linewidth=1, label = 'Non-Hispanic white, single race')
plt.plot(blck['Week'], blck['Value'], 'r-', linewidth=1, label='Non-Hispanic black, single race')
plt.plot(asia['Week'], asia['Value'], 'm-', linewidth=1, label='Non-Hispanic Asian, single race')
plt.plot(oth['Week'], oth['Value'], 'y-', linewidth=1, label='Non-Hispanic, other races and multiple races')
plt.plot(nat_est['Week'], nat_est['Value'], 'k-', linewidth=3, label='National Estimate')
plt.xlabel('Week')
plt.ylabel('Percent denied or did not recieve')
plt.legend(bbox_to_anchor=(1, 1))
plt.show()



non = edu[edu['Subgroup'] == 'Less than a high school diploma']
high = edu[edu['Subgroup'] == 'High school diploma or GED']
somcol = edu[edu['Subgroup'] == '''Some college/Associate's degree''']
bach = edu[edu['Subgroup'] == '''Bachelor's degree or higher''']

plt.plot(non['Week'], non['Value'], 'b-', linewidth=1, label='Less than a high school diploma')
plt.plot(high['Week'], high['Value'], 'g-', linewidth=1, label = 'High school diploma or GED')
plt.plot(somcol['Week'], somcol['Value'], 'r-', linewidth=1, label='''Some college/Associate's degree''')
plt.plot(bach['Week'], bach['Value'], 'm-', linewidth=1, label='''Bachelor's degree or higher''')
plt.plot(nat_est['Week'], nat_est['Value'], 'k-', linewidth=3, label='National Estimate')
plt.xlabel('Week')
plt.ylabel('Percent denied or did not recieve')
plt.legend(bbox_to_anchor=(1, 1))
plt.show()


plt.plot(nat_est['Week'], nat_est['Value'], 'm-', linewidth=2, label='National Estimate')
plt.xlabel('Week')
plt.ylabel('Percent denied or did not recieve')
plt.legend()
plt.show()
