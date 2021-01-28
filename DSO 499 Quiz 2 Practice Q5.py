import numpy as np
import random
#
# def simulate(quantity):
#     cost = 5
#     price = 20
#
#     # determine demand
#     d = np.random.randint(1000, 1500) if np.random.rand() < 0.4 else np.random.randint(300, 500)
#
#     # determine profit
#     return min(quantity, d)*20 - quantity * 5
#
#
# def monte_carlo(quantity, m=1000):
#     mean = np.mean([simulate(quantity) for i in range(m)])
#     return round(mean, 2)
#
#
# def main():
#     print("quantity, profit")
#     bestProfit = 0
#
#     for q in range(300, 1301, 100):
#         p = monte_carlo(q)
#         print(q, p, sep=", ")
#         if p > bestProfit:
#             bestProfit = p
#             bestQuantity = q
#
#     print("The best __...", bestQuantity)
#
# main()

samp = [1,2]
sample = random.sample(samp, 2)
print(sample)