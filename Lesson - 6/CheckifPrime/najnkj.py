from math import sqrt
number=int(input("Enter your number \n"))
if number > 1:
    for i in range(1,int(sqrt(number))+ 1):
        if(number%i==0):
            print(number,"is not a prime")
            break
        else:
            print(number,"is prime")
else:
    print(number,"is not a prime")