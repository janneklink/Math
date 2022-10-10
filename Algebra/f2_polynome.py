def find_primes(n):
    m = pow(2, n + 1)
    possible_primes = [1] * m
    possible_primes[0] = 0
    possible_primes[1] = 0
    for i in range(2, m):
        if possible_primes[i] == 1:
            for j in range(2 * i, m, i):
                pass
    return sum(possible_primes)
