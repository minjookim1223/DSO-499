# If a portfolio manager is deciding when to buy a security or not (especially for bonds),
# he/she could earn information about the security's expected rate of return as well as
# possible future cash flows in order to calculate the present value of the security.
# If the security's present value is higher than the current cost, then he/she
# would buy the security.

# You could essentially put all the expected cashFlows in a list and declare variables for the rate of return,
# totalValue (which would be 0 initially), and i, which will be the parameter of the while loop.
# Then, you would use the while loop to loop through the length of the cash flow list to calculate present value
# of each security, then add it to the totalValue. When you get the total value, you would print it out.


def main():
    # information about the cashFlows of the security
    cashFlows = [100, 400, 300]
    i = 0       # parameter to end i
    r = 0.1     # rate of return
    # a variable that will add up all the present values of cash flows
    totalValue = 0

    # loop through the list of cashFlows
    while i < len(cashFlows):
        # find the present value for each cash flow
        presentValue = cashFlows[i]/((1+r)**(i+1))
        # add the present value to the total value
        totalValue += presentValue

        # parameter to loop through the list
        i += 1

    # list out the totalValue
    print(round(totalValue, 2))


main()


# #2
# Both program A and B are used to see whether password that the user enters match the password that is stored.
# Program A uses while loop to go through three attempts and also while the password and the input do not match.
# i is used as a parameter to count the number of attempts. If the password is guessed correctly by the end of the loop,
# The access is granted. Else, print denied.
# Program B is similar but it uses for loop to go through two attempts. If the input matches the password,
# break out of the loop. If not, take user input after prompting the user by saying incorrect password.
# If the user gets the password correct, access is granted. If not, print denied.

#
