from math import gcd

def Lcm(*n):#Lcm of n arguments

    l = []
    for i in n:
        l.append(i)

    lcm = 1
    for i in l:
        lcm = (lcm * i) // gcd(i, lcm)

    print(f"LCM of {l} is {lcm}")

Lcm(5,2,4)

#OUTPUT
'''
LCM of [5, 2, 4] is 20'''