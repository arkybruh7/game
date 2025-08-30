import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

primes = []
num = 2
while len(primes) < 20:
    if is_prime(num):
        primes.append(num)
    num += 1

print(*primes)