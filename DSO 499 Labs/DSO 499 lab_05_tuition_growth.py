# DSO 499 Lab 05: Tuition growth rate
# Your name: Minjoo Kim
# Your email: minjook@usc.edu

import numpy as np

# input data
start_year = 1985
tuition = [10000, 10750, 11900, 13300, 14250, 15350, 16400, 17500, 18550,
           19750, 21000, 22700, 23840, 25000, 26260, 27250, 28500, 30050,
           31800, 33650, 35600, 37500, 39600, 41900, 43800, 46150, 48600,
           51200, 53500, 56175, 58875, 61225, 63675]


### INSERT YOUR CODE BELOW THIS LINE ###

def main():
    maxGrowth = 0
    growthList = []
    yearOne = 0
    yearTwo = 0
    for i in range(len(tuition)-1):
        growth = 1 + (tuition[i+1]-tuition[i])/tuition[i]
        growthList.append(growth)
        if growth > maxGrowth:
            maxGrowth = growth
            yearOne = 0
            yearTwo = 0
            yearOne += (1985 + i)
            yearTwo += (1986 + i)

    growthListAverage = np.mean(growthList)

    print("The average year-to-year tuition growth rate was", round(growthListAverage, 2))
    print("The maximum growth rate was", round(maxGrowth, 2), "from", yearOne, yearTwo)

main()
