import random

def NOD(a,b):
    while a > 0 and b > 0:
        if a > b: a%= b;
        else: b%= a;
    return a + b;

def sum(arr, n):
    summa = 0;

    for i in range(n):
        summa += arr[i];
    return summa;

def checkPrime(value):
    if value > 1:
        if value % 2 == 0:
            return value == 2
        d = 3
        while d * d <= value and value % d != 0:
            d += 2
        return d * d > value
    else: return False

def toBinary(str):
    str1 = " ".join(f"{ord(i):08b}" for i in str)
    return str1;

def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def nextPrime(value):
    if value == 1: return 2;
    if value == 2: return 3;
    if checkPrime(value) == 1: value = value + 1;
    i = value;
    while True:
        if checkPrime(i):
            return i;
        i = i + 1;

def superSequence(n):
    arr = [0] * n
    arr[0] = 1
    chislo = 10
    for i in range(1, n):
        arr[i] = random.randrange(sum(arr, n) + 1, chislo)
        chislo = chislo + sum(arr, n)
    return arr