def factorial(n: int) -> int:
    """Compute the factorial of a number if it is possible (above zero)"""
    if n < 0:
        raise Exception("Negative numbers don't have factorial")
    else:
        result: int = 1
        for i in range(1, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    num: int = int(input("Enter a number: "))
    print(factorial(num))
