a = 2**31 -1
c = 12345
m = 2**128

def gcd(a, b):
    if b == 0:
        print a
        return a
    else:
       return gcd(b, a% b)

def fermat(n, t):
    for i in range(0, t):
        a = lcg(101)
        if

def lcg(seed):
    for i in range(0,100):
        seed = (a*seed + c) % m
        print seed
    return seed

gcd(1071, 462)
