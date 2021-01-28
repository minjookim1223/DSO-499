x = [1, '2', 3.4]
for i in range(2):
    x.append(i)

x[2] -= x[-1]
print(len(x))
print(x[2])
print(type(x[1]))
print(sum(x[3:]))
print(x[0] // 2 == x[-1] ** 2)
print(x[-1:] + x[:-1])

print("")

prices = [6.71, 6.65, 5.95, 4.4, 2.09, 1.7]
ma = []
n = 3
for i in range(4):
    ma.append(round(sum(prices[i:(i + 3)]) / 3, 2))
print(ma[len(ma) - 1])
print(ma)
print("")