# DSO 499 Lab 06: Tuition forecast
# Your name
# Your email

import numpy as np

# input data
start_year = 1985
tuition = [10000, 10750, 11900, 13300, 14250, 15350, 16400, 17500, 18550,
           19750, 21000, 22700, 23840, 25000, 26260, 27250, 28500, 30050,
           31800, 33650, 35600, 37500, 39600, 41900, 43800, 46150, 48600,
           51200, 53500, 56175, 58875, 61225, 63675]
alpha = 0.8

# output header
print('Year, Forecast, Actual')

# output first year
print(start_year, 'None', tuition[0], sep=', ')

# output second year
year = start_year + 1
forecast = tuition[0]
actual = tuition[1]
print(year, forecast, actual, sep=', ')

### INSERT YOUR CODE BELOW THIS LINE ###
year = start_year + 2       # the year starts from 1987 since 1985 and 1985 have been hard coded

forecastList = ["None", 10000] # create a list for all the forecasts

# Since the first two forecasts have been hard coded, the loop should start at 2
for i in range(2, len(tuition)+1):
    # calculate the forecast
    Ft = 0.8*(tuition[i-1]) + (1-0.8)*forecastList[i-1]
    # append the result to the list
    forecastList.append(Ft)

    # print the year
    print(year, end=", ")
    # followed by the forecast
    print(round(forecastList[i]), end=", ")

    # actual tuition
    # make sure to use if statement to account for the last "actual"
    # so that it appear as "?"
    if i < len(tuition):
        print(tuition[i])
    else:
        print("?")
    # add 1 to the year to match the next element
    year = year + 1
