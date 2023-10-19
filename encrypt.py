def encrypt(p, cycle, count1, cleancipher, arr, m , q, n):
    cipher2 = ""
    if p == cycle - 1:
        cipher2 = cleancipher[count1:]
        h = len(cipher2)
        c = 0
        count = 0
        for i in range(h):
            c += (ord(cipher2[i]) - 48) * arr[count]
            count += 1
    else:
        cipher2 = cleancipher[count1:count1+n]
        c = 0
        count = 0
        for i in range(n):
            c += (ord(cipher2[i]) - 48) * arr[count]
            count += 1
    
    dc = c * m % q
    counter = dc
    print("шифртекст символа: ", c, ", counter: ", counter)
    return counter, c