def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(limit):
    return sum(n for n in range(2, limit + 1) if is_prime(n))

# Set the limit to 2,000,000
limit = 2000000
print("Sum of prime numbers up to", limit, "is:", sum_of_primes(limit))
