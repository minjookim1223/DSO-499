# Lab 18: Tap card
# Your name: Minjoo Kim (Jay)
# Your email: minjook@usc.edu

### INSERT YOUR CODE BELOW THIS LINE ###
class TapCard:
    def __init__(self):
        print("Congratulations!")
        self.value = 0

    def reload(self):
        temp = int(input("Enter amount to reload: "))
        self.value += temp

    def tap(self):
        if self.value >= 1.75:
            self.value -= 1.75
        else:
            print("Tap denied: Insufficient stored value!")

    def __str__(self):
        msg = "Stored value: $" + str(round(self.value, 2))
        return msg

### INSERT YOUR CODE ABOVE THIS LINE ###

# initialize tap card
x = TapCard()

# keep performing user-specified actions until user quits
action = None
while action != 'q': 

    # print stored value and menu
    print('----------')
    print(x)
    print('Menu:')
    print('    (R)eload value')
    print('    (T)ap for Metro ($1.75)')
    print('    (Q)uit')

    # prompt user for action (and convert to lower case)
    action = input('What would you like to do? ').lower()
    
    # perform action
    if action == 'r':   # reload
        x.reload()

    elif action == 't': # tap
        x.tap()
    
    elif action == 'q': # quit
        print('Goodbye!')

    else:               # invalid action
        print('Invalid action. Please try again. ')