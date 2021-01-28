# Lab 11: Number Guessing - For
# Minjoo Kim (Jay)
# minjook@usc.edu
import numpy as np
import random


def main():
    randNum = np.random.randint(100)

    for i in range(7):
        user = int(input("(Attempt " + str(i+1) + ") Make a guess: "))
        if user > randNum:
            print("Enter a smaller number.")
        elif user < randNum:
            print("Enter a larger number.")
        else:
            print("Correct!")
            break
        if i == 6:
            print("You lost!")


main()
