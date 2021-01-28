# Lab 13: Stock simulation revisited
# Your name
# Your email

import numpy as np

### INSERT YOUR CODE BELOW THIS LINE ###

def simulate(S_init, upper, lower, a_list, b_list, prob_good): 
    """
    Simulate one sample of the given stock trading strategy. 
    
    INPUT ARGUMENTS
        S_init: Initial investment. 
        upper: Upper threshold for quitting. 
        lower: Lower threshold for quitting. 
        a_list: List of parameter a values ("Good", "Bad"). 
        b_list: List of parameter b values ("Good", "Bad"). 
        prob_good: Probability of a "Good" year. 
        
    RETURN VALUE
        Simulated trading strategy outcome, 'Winning' or 'Losing'. 
    """

    # initialize first day
    day = 0
    S = S_init

    # trade until either threshold is exceeded
    while S <= upper and S >= lower: 
        # increment day
        day += 1
        
        # simulate economy
        r = np.random.rand()
        a = a_list[0] if r < prob_good else a_list[1]
        b = b_list[0] if r < prob_good else b_list[1]
        
        # update stock value
        S *= np.exp( a + b * np.random.randn() )
    
    # return winning/losing case
    return 'Winning' if S > upper else 'Losing'


def monte_carlo(n_samples): 
    """
    Count the stock trading strategy outcomes for multiple samples. 
    
    INPUT ARGUMENT
        n_samples: Number of samples to simulate. 
    
    RETURN VALUE
        count: A dictionary with outcomes as keys and counts as values. 
    """
    
    # initialize empty dictionary as counter
    count = {}
    
    # count outcomes for n_samples simulations
    for i in range(n_samples): 
        outcome = simulate(10, 200, 1, [0.48, -0.22], [0.23, 0.79], 0.24)
        count[outcome] = count.get(outcome, 0) + 1
    
    # return counter dictionary
    return count

### INSERT YOUR CODE ABOVE THIS LINE ###

def main():

    # get user input on number of samples
    n_samples = int(input('Enter number of samples: '))

    # get dictionary with sample counts of outcomes
    count = monte_carlo(n_samples)
    
    # output simulated probabilities, in alphabetical order of outcomes
    for k in sorted(count):
        p = round(count[k]/n_samples*100, 2)
        print(k, ':', p, '%')

help(simulate)
help(monte_carlo)
main()