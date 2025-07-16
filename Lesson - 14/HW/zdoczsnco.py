def recursive_input_collector(numbers_list=None):
    if numbers_list is None:
        numbers_list = []

    try:
        num = int(input("Enter a number (enter a negative number to stop): "))
        if num < 0:
            print("Negative number entered. Stopping input collection.")
            return numbers_list
        else:
            numbers_list.append(num)
            return recursive_input_collector(numbers_list)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return recursive_input_collector(numbers_list)

if __name__ == "__main__":
    print("Starting recursive input collection.")
    collected_numbers = recursive_input_collector()
    print("Numbers collected (excluding the negative stop number):", collected_numbers)