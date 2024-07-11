numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
primes_not_primes_dict = {}
is_primes = True

for i in numbers:
    if i != 1:
        primes_not_primes_dict.update({i: is_primes})

for i in list(primes_not_primes_dict.keys()):
    for j in range(2, i):
        if i % j == 0:
            primes_not_primes_dict.update({i: False})
            break

for i in list(primes_not_primes_dict.keys()):
    if primes_not_primes_dict[i] == is_primes:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes: ', primes)
print('Not Primes: ', not_primes)
