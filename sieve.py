"""Sieve of Eratosthenes + variants — prime number generation."""
def eratosthenes(n):
    if n < 2: return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, v in enumerate(is_prime) if v]

def segmented_sieve(lo, hi):
    primes = eratosthenes(int(hi**0.5) + 1)
    is_prime = [True] * (hi - lo + 1)
    if lo <= 1:
        for i in range(max(0, 2 - lo)):
            is_prime[i] = False
    for p in primes:
        start = max(p * p, ((lo + p - 1) // p) * p)
        for j in range(start, hi + 1, p):
            is_prime[j - lo] = False
    return [lo + i for i, v in enumerate(is_prime) if v]

if __name__ == "__main__":
    p = eratosthenes(100)
    print(f"Primes up to 100: {p}")
    assert len(p) == 25
    assert p[:5] == [2, 3, 5, 7, 11]
    seg = segmented_sieve(100, 200)
    print(f"Primes 100-200: {seg}")
    assert 101 in seg and 197 in seg
    assert len(eratosthenes(1000000)) == 78498
    print("All tests passed!")
