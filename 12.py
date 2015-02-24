# ProjectEuler.net
# Problem 12
#
# Highly divisible triangular number


def primes_sieve(limit):
    primes = []
    a = [True] * limit
    a[0] = a[1] = False
    for i, isprime in enumerate(a):
        if isprime == True:
            primes.append(i)
            for n in xrange(i*i, limit, i):
                a[n] = False
    return primes


if __name__ == "__main__":
    primes = primes_sieve(28)
    print primes