import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score
"""Although this function is specific to testing SVI and Poverty Status against covid mortality, its general
structure can be used for any multivariable linear regression problem. Simply replace the testing_df[] columns with
other variables and the X variable, and the function will test for those instead."""

# Reads in the csv files
df = pd.read_csv('death_rate.csv')

# Isolates variables that will be involved in testing
testing_df = df[['SVIPercentile', 'POVERTY_STATUS_Below_100_Percent_Level', 'covid_mortality_rate']]

# Creates independent (explanatory) and dependent variables
X = testing_df[['SVIPercentile', 'POVERTY_STATUS_Below_100_Percent_Level']]
y = testing_df['covid_mortality_rate']

# Trains the Linear Regression model using the train_test_split() function and fits the model to the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)
regr = LinearRegression()
regr.fit(X_train, y_train)

# Calculates the coefficients of each of the explanatory values and prints them along with the r^2 value
coeff_testing_df = pd.DataFrame(regr.coef_, X.columns, columns=['Coefficient'])
print(coeff_testing_df)
print(regr.score(X_test, y_test))

# Prints a list for checking: includes on the left, actual values, on the right, predicted values for that datapoint
y_pred = regr.predict(X_test)
predicting_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(predicting_df)

# Prints r^2 value as a double check, and prints MAE, MSE, and RMSE values
print(r2_score(y_test, y_pred))
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
