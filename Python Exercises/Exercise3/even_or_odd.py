def even(n):
    if (n % 2) == 0:
        return "{0} is Even".format(n)
    else:
        return "{0} is Odd".format(n)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(even(num))
