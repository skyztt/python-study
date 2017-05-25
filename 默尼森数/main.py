import math

def isPrime(val):
    if val in [2, 3, 5, 7, 11]:
        return True
    if not (val % 2):
        return False
    for i in range(3, int(math.sqrt(val) + 1), 2):
        if not (val % i):
            return False
    return True

def prime(num):
    if num == 1:
        return 2
    num -= 1
    val = 3
    while num:
        if isPrime(val):
            num -= 1
            if num == 0:
                break
        val += 2
    return val

def monisen(no):
    if no <= 0:
        return 0
    p = 0
    i = 1
    while no:
        p = 2**prime(i) -1
        if isPrime(p):
            no -= 1
        i += 1
    return  p

while True:
    i = int(input())
    m = monisen(i)
    print(m)