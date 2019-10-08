import is_prime


def get_prime_factors(n):
    """Tests all divisors of n that are lower or equal than n/2 and if they are prime, returns them"""
    factors = []  # Store prime factors

    for i in range(2, n//2+1):
        if n % i == 0 and is_prime.is_prime (i):
            factors.append(i)
    return factors


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(get_prime_factors(num))
