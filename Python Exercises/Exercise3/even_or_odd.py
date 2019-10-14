def even(n):
    """Print return whether if a number is even or odd"""
    if (n % 2) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if even(num):
        print ("{} is Even".format(num))
    else:
        print ("{} is Odd".format(num))
