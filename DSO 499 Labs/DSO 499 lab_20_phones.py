# Lab 20: Phones and smartphones
# Your name
# Your email

class Phone: 
    
    def __init__(self): 
        self.call_time = 0
        self.text_count = 0
    
    def __str__(self): 
        return 'Usage summary: call = ' + str(self.call_time) + ', text = ' + str(self.text_count)
    
    def call(self, time=1): 
        self.call_time += time
    
    def text(self): 
        self.text_count += 1


### INSERT YOUR CODE BELOW THIS LINE ###
class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.data = 0

    def use_data(self, data):
        self.data = data

    def __str__(self):
        msg = 'Usage summary: call = ' + str(self.call_time) + ', text = ' + str(self.text_count) +\
              (', data = ' + str(self.data))
        return msg


### INSERT YOUR CODE ABOVE THIS LINE ###

x = SmartPhone()
x.call(29)
x.text()
x.use_data(208)
x.text()
print(x)