import is_prime


def get_prime_factors(n):
    """Tests all divisors of n that are lower or equal than n/2 and if they are prime, returns them"""
    factors = []  # Store prime factors

    # Start testing from 2 up to half of the target number,
    # the maximum possible prime factor
    for i in range(2, n // 2 + 1):
        if n % i == 0 and is_prime.is_prime(i):  # If number is a divisor and is prime, return it
            factors.append(i)
    return factors


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(get_prime_factors(num))
