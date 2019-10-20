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


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(is_prime(n))
