# Baby girl name generator
# Minjoo Kim
# minjook@usc.edu

import numpy as np

"""This function chooses chooses a random key from a given dictionary using discrete random distribution.
First, the function creates a variable n, which adds all the numbers of recurring alphabets according to the given
dictionary and chooses random number from [0, sum(d.values)).
Second, the function loops through the dictionary and subtracts the value of the keys from n.
When, n becomes less than 0, the key will be then returned to be used for generate_next() method in Letter class
in order to generate the next letter for a given alphabet. """
def choose_from_dict(d):
    n = np.random.randint(sum(d.values()))
    for k, v in d.items():
        n = n - v
        if n < 0:
            break
    return k


class Letter:
    """The constructor takes in the letter parameter. It instantiates two variables: self.letter, which is a letter
    that we are looking at in order to produce the next letter. self.next_letter will is a dictionary that will hold
    the alphabets that come after self.letter as keys and the number of occurrences of those alphabets as values"""
    def __init__(self, letter):
        self.letter = letter
        self.next_letter = {}

    """This method will be used in the main function to update the dictionary that is assigned to each object.
    If the letter provided does not exist, the default value of that letter key becomes 0. If that value is provided as
    a parameter, then the value increments by 1"""
    def add_next(self, letter):
        self.next_letter[letter] = self.next_letter.get(letter, 0) + 1

    """This method utilizes choose_from_dict() function as it passes the dictionary given in order to choose the
    next letter."""
    def generate_next(self):
        return choose_from_dict(self.next_letter)

    """When the user prints the object, the program will return the message provided in this method. In this case,
    The function would return the letter current letter that we are looking at (self.letter) and the dictionary of the
    given letter casted into string. This could be used to print out the letter needed to create the name one by one.
    """
    def __str__(self):
        return self.letter + str(self.next_letter)


# parse input file as a list of names
with open('baby_girl_names_2018.csv', 'r') as f:
    name_list = f.read().upper().split()

## INSERT YOUR CODE BELOW THIS LINE ###


def main():
    repeat = ""         # This parameter is used to keep track whether the user wants to continue creating new names

    # Continue the program as long as the user presses Enter
    while repeat == "":

        final_name = ""                             # An empty string to create a new name

        # We are not given a first letter to pass into the class Letter.
        # Thus, we have to come up with our own first letter given the discrete random distribution
        first_letter_dict = {}                          # Create an empty dictionary for the first letter
        for name in name_list:                                  # Loop through each name in the list
            # Same idea with add_next() method.
            # Go through all the first letters and update the dictionary accordingly
            first_letter_dict[name[0]] = first_letter_dict.get(name[0], 0) + 1
        # Choose the first letter from the dictionary
        first_letter = choose_from_dict(first_letter_dict)
        # Add the letter to the name
        final_name += first_letter

        # Now you are given a letter to create an object.
        given_letter = first_letter

        while given_letter != "":                           # While you are given a letter:
            letter_object = Letter(given_letter)            # create a Letter object by passing the given_letter
            for name in name_list:                          # Loop through all the names in the name_list
                for i in range(len(name)):                  # Loop through each letters in each name in the list
                    if name[i] == given_letter:             # If the letter matches the given letter,
                        if (i + 1) == len(name):            #   If the current letter is at last index,
                            letter_object.add_next("")      #       then no alphabet is added to the dictionary (attach "" instead).
                        elif name[i + 1].isalpha():         #   else if, the next letter is an alphabet,
                            letter_object.add_next(name[i+1])       # Update the dictionary with the new letter using add.next() method
            new_letter = letter_object.generate_next()      # Generate a new letter using generate_next() method
            final_name += new_letter                        # Add the new letter to the final name
            given_letter = new_letter                       # Since we have to see what comes after the new letter,
                                                                    # the given_letter becomes the new letter.

        # When you are done, print out the final name
        print(final_name)
        # Ask the user whether to generate a new name or not
        repeat = input("Press Enter to generate another name, or any other key to quit: ")


main()
