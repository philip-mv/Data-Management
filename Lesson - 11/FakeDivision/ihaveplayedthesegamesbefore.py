def divide(ourdividend, ourdivisor):
    if ourdivisor == 0:
        raise ZeroDivisionError("division by zero")
    sign = -1 if ((ourdividend < 0) ^ (ourdivisor < 0)) else 1
    ourdividend = abs(ourdividend)
    ourdivisor = abs(ourdivisor)

    quotientNumber = 0
    tempNumber = 0
    for i in range(31, -1, -1):
        if tempNumber + (ourdivisor << i) <= ourdividend:
            tempNumber += ourdivisor << i  # FIX: use << i, not << 1
            quotientNumber |= 1 << i
    if sign == -1:
        quotientNumber = -quotientNumber
    return quotientNumber

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("Result of", a, "/", b, "is", divide(a, b))
