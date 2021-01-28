# Lab 12: Stock simulation
# Your name
# Your email

import numpy as np

# input data
S_init = 10    # initial investment
upper = 200    # upper threshold for quitting
lower = 1      # lower threshold for quitting
a_list = [0.48, -0.22]   # list of possible values for parameter a
b_list = [0.23, 0.79]    # list of possible values for parameter b
prob_good = 0.24         # probability of a year being "Good"

# print header
print('day, value')

### INSERT YOUR CODE BELOW THIS LINE ###

# initial and print first day
day = 0
S = S_init
print(day, S, sep=', ')

# trade until either threshold is exceeded
while upper >= S >= lower:
    # increment day
    day += 1
    
    # simulate economy
    r = np.random.rand()
    a = a_list[0] if r < prob_good else a_list[1]
    b = b_list[0] if r < prob_good else b_list[1]
    
    # update stock value
    S *= np.exp( a + b * np.random.randn() )
    
    # output results for the day
    print(day, round(S, 2), sep=', ')

# output winning/losing case
print('Winning' if S > upper else 'Losing', 'case')