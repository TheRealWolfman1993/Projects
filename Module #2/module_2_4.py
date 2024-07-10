numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in range(2, 16):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
       print ('Primes: ', num)
for num in range(2, 16):
    prime = False
    for i in range(2, num):
        if (num % i == 0):
            prime = True
    if prime:
        print ('Not Primes: ', num)