def CheckifSame(number1,number2):
    if((number1 ^ number2)!=0):
        print("Number1 not equal to Number 2")
    else:
        print("Number 1 = Number 2")
number1 = int(input("Enter the first number for comparision :"))
number2 = int(input("Enter the second number for compariosion :"))
CheckifSame(number1,number2)