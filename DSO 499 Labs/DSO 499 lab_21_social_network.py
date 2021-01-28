# Lab 21: Social network
# Your name: Minjoo Kim
# Your email: minjook@usc.edu


class User:

    def __init__(self, name):
        """ Initialize name and empty list of friends. """
        self.name = name
        self.friends = []

    def __str__(self):
        """ String representation. """
        s = self.name + ' has ' + str(len(self.friends)) + ' friend(s): '
        s += ', '.join(self.friends)
        return s

    def add_friend(self, name):
        """ Add a friend by name to list of friends. """
        self.friends.append(name)


def friend(a, b):
    a.add_friend(b.name)
    b.add_friend(a.name)

### INSERT YOUR CODE BELOW THIS LINE ###

class Friends(User):
    def check(self, name):



def main():
    users = []
    users = 

main()