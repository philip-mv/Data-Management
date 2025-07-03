def powerof8(number):

    count = 0


    if number <= 0:
        return False


    if (number & (number - 1)) != 0:
        return False


    while(number > 1):
        number >>= 1
        count += 1


    if(count % 3 == 0):
        return True
    else:
        return False

try:
    user_number = int(input("Enter your number: "))


    if(powerof8(user_number)):
        print(f"Yes, {user_number} is a power of 8")
    else:
        print(f"No, {user_number} is not a power of 8")

except ValueError:

    print("Invalid input. Please enter a valid integer.")
