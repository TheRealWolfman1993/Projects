numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers1 = list()
numbers2 = list()
for num in range(2, 16):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
       numbers1.append(num)
for num in range(2, 16):
    prime = False
    for i in range(2, num):
        if (num % i == 0):
            prime = True
    if prime:
        numbers2.append(num)
print("Primes:",numbers1)
print("Not Primes:",numbers2)
