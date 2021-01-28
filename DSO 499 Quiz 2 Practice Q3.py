c = 2.54


def inch_to_cm(x=0):
    y = x*c
    return y


x = 2
z = inch_to_cm(x)
d = inch_to_cm()

print(x)
print(y)
print(z)
print(c)
print(d)

# 1. x = 2
# 2. Error
# 3. z = 5.08
# 4. c = 2.54
# 5. d = 0

def fever(temp, low=98.6, high=100.4):
    if temp > high:
        x = 'High'
    elif temp > low:
        x = 'Low'
    else:
        x = 'No'
    print(x, 'fever')

fever(98)

# 6. temp, low = 98.6, high = 100.4
# 7. temp > high
# 8. temp > low
# 9. No fever
# 10. Low fever