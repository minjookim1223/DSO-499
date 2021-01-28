# Lab 17: Student participation
# Your name: Minjoo Kim (Jay)
# Your email: minjook@usc.edu

### INSERT YOUR CODE BELOW THIS LINE ###


class Student:
    def __init__(self, name):
        self.count = 0
        self.name = name

    def speak(self):
        self.count += 1

    def __str__(self):
        if self.count == 1:
            msg = self.name + " spoke up to " + str(self.count) + " time"
        else:
            msg = self.name + " spoke up to " + str(self.count) + " times"
        return msg

a = Student('Alice')
b = Student('Bob')

### INSERT YOUR CODE ABOVE THIS LINE ###

print(a)
print(b)

a.speak()
b.speak()
a.speak()

print(a)
print(b)