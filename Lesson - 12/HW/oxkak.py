def find_all_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substrings.append(s[i:j+1])
    return substrings

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = find_all_substrings(input_string)
    print("All substrings:")
    for sub in result:
        print(sub)