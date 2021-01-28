import numpy as np

# input parameters
a = 0.5     # average patient inter-arrival time (minutes)
h = 6       # number of hours the clinic is open


def simulate():
    duration = h*60
    patients = 0

    while duration >= 0:
        timeBetween = np.random.exponential(a)
        if duration > timeBetween:
            duration -= timeBetween
            patients += 1
            print(duration, timeBetween, patients, sep=", ")
        else:
            break

    return patients


def monte_carlo(m):
    """ Return the average patients served for m samples. """
    return np.mean([simulate() for i in range(m)])

print('Average patients served:', monte_carlo(100))