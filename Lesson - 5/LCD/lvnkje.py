def calculate_hcf(a, b):
    
    if a < b:
        a, b = b, a

    while b:
        
        temp_b = b
       
        b = a % b
       
        a = temp_b
    return a

def calculate_lcm(num1, num2):
  
    if num1 == 0 or num2 == 0:
        return 0
    
   
    hcf = calculate_hcf(abs(num1), abs(num2)) 
    
    lcm = (abs(num1) * abs(num2)) // hcf
    return lcm


try:
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))

  
    lcm_result = calculate_lcm(number1, number2)
    print(f"LCM of {number1} and {number2} = {lcm_result}")

except ValueError:
    print("Invalid input. Please enter integer numbers only.")
except Exception as e:
    print(f"An error occurred: {e}")
