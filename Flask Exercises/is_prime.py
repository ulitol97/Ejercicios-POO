"""Module containing the logic to operate with number to check if they are prime and get their prime factors"""


def is_prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):  # Check from 2 to all numbers excluding the number itself
            if (num % i) == 0:
                return False
        return True

    # if input number is <= to 1, it is not prime
    else:
        return False


def get_prime_factors(n):
    """Tests all divisors of n that are lower or equal than n/2 and if they are prime, returns them"""
    factors = []  # Store prime factors

    # Start testing from 2 up to half of the target number,
    # the maximum possible prime factor
    for i in range(2, n // 2 + 1):
        if n % i == 0 and is_prime(i):  # If number is a divisor and is prime, return it
            factors.append(i)
    return factors
