
a = int(input("Enter 'a' for a^b : "))
b = int(input("Enter 'b' for a^b : "))

result = a ** b


def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

if is_power_of_2(result):
    print(f"{a}^{b} = {result} is a power of 2")
else:
    print(f"{a}^{b} = {result} is not a power of 2")