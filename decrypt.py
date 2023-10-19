from dataclasses import dataclass

def decrypt(counter, arr, c, n):
    decipher = ""
    cipher = ""
    ciph2 = ""
    maximus = 0
    arr3 = [0] * 24
    e = 0

    while counter != 0:
        for i in range(n):
            maximus = arr[i]
            if maximus > counter:
                maximus = arr[i - 1]
                break

        counter = counter - maximus
        arr3[e] = maximus
        maximus = 0
        e += 1

    class Array:
        def __init__(self, digit, flag):
            self.digit = digit
            self.flag = flag

    decarr = [0] * n
    for i in range(n):
        decarr[i] = Array(arr[i], False)

    for i in range(n):
        for j in range(n):
            if arr3[i] == decarr[j].digit:
                decarr[j].digit = 1
                decarr[j].flag = True

    for i in range(n):
        if decarr[i].flag != True: decarr[i].digit = 0

    for i in range(n):
        ciph2 += str(decarr[i].digit)

    decipher += ciph2
    #print(decipher)
    cipher += str(c)
    return decipher, cipher