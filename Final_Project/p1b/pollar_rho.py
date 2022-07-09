import math
import random


def roh(n):
    i = 1
    x = random.randint(0, n-1)
    y = x
    k = 2
    while True:
        i += 1
        x = (pow(x, 2)-1) % n
        d = math.gcd(y-x, n)
        if d != 1 and d != n:
            return d
        if i == k:
            y = 2*x
            k *= 2


print(roh(98834976202698839303077))
