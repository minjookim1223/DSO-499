# Lab 14: Secretary problem helper functions
# Your name
# Your email

import numpy as np

def simulate(r): 
    """
    Simulate the outcome of a Secretary problem. 
    
    INPUT ARGUMENTS
        r:  Rejection ratio (proportion of applicants to reject initially)
        
    RETURN VALUE
        True if the best applicant was hired, False otherwise. 
    """

    # generate list of random scores
    n = 100                               # number of applicants
    score = np.random.rand(n)             # list of n random scores
    
    # reject initial applicants
    n_rejected = int(n * r)               # number of initial applicants rejected
    best_score = max(score[:n_rejected])  # best score among rejected

    # keep interviewing while next applicant doesn't score better and there are applicants remaining
    i = n_rejected    # next applicant to interview
    while score[i] <= best_score and i < n-1: 
        i += 1
    # at the end of the loop, i will be the index of the hired applicant

    # return whether or not the hired applicant was the true best applicant
    return i == np.argmax(score)


def monte_carlo(m, r): 
    """
    Use Monte Carlo simulate to estimate the success rate for a Secretary problem. 
    
    INPUT ARGUMENTS
        m:  Number of samples to simulate. 
        r:  Rejection ratio (proportion of applicants to reject initially)
        
    RETURN VALUE
        The success rate (proportion of optimal hires) across all simulated samples. 
    """
    return np.mean([ simulate(r) for i in range(m) ])
