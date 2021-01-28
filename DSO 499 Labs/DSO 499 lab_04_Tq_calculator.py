# Lab 04 - Waiting time calculator
# Minjoo Kim (Jay)
# minjook@usc.edu

prompt = 'Number of machines = '

### INSERT YOUR CODE BELOW THIS LINE ###


def main():
    a = 5       # a = average inter-arrival time of customers
    p = 3       # p = average service time
    CVa = 0.8   # CVa = coefficient of variation for inter-arrival time
    CVp = 1     # CVp = coefficient of variation for service time
    u = p/a     # u = utilization (p/a)

    # loop through the range 1 - 5 (excluding 6), taking 1 step at a time
    for m in range(1, 6):
        # calculate the first fraction, p/m
        factorOne = p/m
        # calculate the second fraction
        factorTwo = u**((2*(m+1))**.5-1)/(1-u)
        # calculate the third fraction
        factorThree = (CVa**2 + CVp**2)/2

        # Multiply the fractions to complete the equation and calculate Tq
        T = factorOne * factorTwo * factorThree
        # print out the prompt as well as m
        # sample output: Number of machines = 1
        print(prompt + str(m))
        # print each result according to the number of machines
        # round to nearest hundredth digit
        print(round(T, 2), "\n")


main()
