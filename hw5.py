D = 74020964815951
M1 = ""
while D > 0:
    M1 = chr(D & 0xff) + M1
    D = D >> 8
print(M1)
