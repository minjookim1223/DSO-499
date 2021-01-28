# Lab 15: Payday
# Minjoo Kim
# minjook@usc.edu

### INSERT YOUR CODE BELOW THIS LINE ###


def payday(h, w, r=1.5, t=40):
    # if you worked longer than t threshold, count for over time
    if h > t:
        pay = w*t + w*r*(h-t)
    # else, do not count for over time
    else:
        pay = w*t

    return pay

### INSERT YOUR CODE ABOVE THIS LINE ###


# test cases
print(payday(10, 15))
print(payday(50, 10))
print(payday(50, 10, 2))
print(payday(80, 100, t=60))
