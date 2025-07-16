def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    number = 5  
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")

    number = 0
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")

    number = 7
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")