import random
import math
import os
from bonusfunction import toBinary, superSequence, nextPrime, NOD, mulinv
from encrypt import encrypt
from decrypt import decrypt

#arr = [1,2,3,4,5,6,7,8]

r = 0;
str1 = os.getenv("message")
print("Бинарный вид: ", toBinary(str1))

n = int(os.getenv("n"))
arr = superSequence(n)

print("Получившаяся последовательность: ", arr)

q = nextPrime(sum(arr, n))
r = random.randrange(2, q)

while NOD(q, r) != 1: r = random.randrange(2, q)
print("Найдены следующие взаимно простые числа: q:", q, "r: ", r)

arr1 = [0] * n
for i in range(len(arr1)):
    arr1[i] = (r * arr[i]) % q
print("Открытый ключ: ", arr1)

m = mulinv(r, q)
print("Обратное число r(mod)q: ", m)

ciph = ""
decipher1 = ""
decipher2 = ""
cipher2 = ""

cipher3 = toBinary(str1)
cleancipher3 = cipher3.replace(' ', '')
strlen = len(str1)
count1 = 0
cycle = math.ceil((strlen * 8.0) / n)
for p in range(cycle):
    counter, c = encrypt(p, cycle, count1, cleancipher3, arr1, m , q, n)
    count1 += n
    decipher, cipher = decrypt(counter, arr, c, n)
    decipher2 += decipher
    cipher2 += cipher
    print(decipher)

symbol1 = 0
ciph = decipher2
kk = 0
ko = 0
for i in range(strlen):
    while kk != 8:
        symbol1 += (ord(ciph[ko]) - 48) * pow(2, 8 - kk - 1)
        kk += 1
        ko += 1

    decipher1 += chr(symbol1)
    kk = 0
    symbol1 = 0


print("Зашифрованный текст: ", cipher2)
print("Расшифрованный текст: ", decipher1)