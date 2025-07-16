def recursive_list_length(input_list):
    if not input_list:
        return 0
    else:
        return 1 + recursive_list_length(input_list[1:])

if __name__ == "__main__":


    my_list = [1, 2, 234, 234, 745, 3, 6, 653]


    length = recursive_list_length(my_list)
    print(f"Length of array: {length}")

    empty_list = []
    length_empty = recursive_list_length(empty_list)
    print(f"Length of empty array: {length_empty}")

    another_list = ['a', 'b', 'c', 'd']
    length_another = recursive_list_length(another_list)
    print(f"Length of another array: {length_another}")