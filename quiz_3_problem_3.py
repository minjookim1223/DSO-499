# Stock investment strategy simulation
# Your name: Minjoo Kim
# Your email: minjook@usc.edu

import numpy as np

# problem data
npv_1 = 100     # initial net present value of first stock
a_1 = 0.05      # parameter "a" of first stock
b_1 = 0.23      # parameter "b" of first stock
npv_2 = 100     # initial net present value of second stock
a_2 = 0.02      # parameter "a" of second stock
b_2 = 0.79      # parameter "b" of second stock
v = 1           # value to invest each day
sim_days = 100      # number of days to simulate


### INSERT YOUR CODE BELOW THIS LINE ###
class Stock:                                    # class created
    def __init__(self, npv, a, b):              # __init__ method to instantiate all the attributes
        self.npv = npv                          # Each stock's NPV
        self.a = a                              # Each stock's a parameter
        self.b = b                              # Each stock's b parameter

    # This method would calculate the new daily npv for each stock
    def calculate_new_npv(self):
        self.npv *= np.exp(self.a + self.b * np.random.randn())
        return self.npv

    # This method would be used to add v if the right condition is met in the main function
    def add_value(self):
        self.npv += v


def main():
    # list created to hold unknown number of stocks
    # making a list would make it easier for the user to analyze more stocks if necessary
    stock_list = []
    total_npv = 0       # total_npv will be used to calculate the total npv at the end of the program

    stock_1 = Stock(npv_1, a_1, b_1)        # Based on information given about two stocks' NPVs, a's, and b's,
    stock_2 = Stock(npv_2, a_2, b_2)        # create objects for both.

    stock_list.append(stock_1)          # Append the objects into the list
    stock_list.append(stock_2)

    # Loop the analysis over sim_days given
    for days in range(sim_days):
        highest_npv = 0                 # highest_npv would be the highest daily NPV for the stocks in the list
        index = 0                       # the variable index is used to see which stock in the list had the highest NPV

        # For each day in sim_days, loop through the list of stocks
        for i in range(len(stock_list)):

            # Calculate the npv for each stock in the list
            new_npv = stock_list[i].calculate_new_npv()
            if new_npv > highest_npv:       # If the NPV calculated is bigger than the one that was the highest,
                index = i                   # return that index. highest_npv will then become the NPV calculated
                highest_npv = new_npv

        # After all the comparison is done for the day, add a dollar to the NPV
        # whose index in the list had the greatest NPV
        stock_list[index].add_value()

    # After the simulation, calculate the total NPV
    for stock in stock_list:
        total_npv += stock.npv

    # Print out the total NPV and round it.
    print("Total final NPV:", round(total_npv, 2))


main()
