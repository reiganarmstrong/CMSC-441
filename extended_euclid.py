# Python program to demonstrate working of extended
# Euclidean Algorithm

# function for extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


# Driver code
a, b = 65537, (58795931-1)*(338715989-1)
# g, x, y = gcdExtended(a, b)
# print("gcd(", a, ",", b, ") = ", g)
# print('x = ', x)
print(pow(4176229917282169, 13082165747160793, 19915121917840759))
