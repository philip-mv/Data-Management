def find_paths(n, m, current_path="", row=0, col=0):
    if row == n - 1 and col == m - 1:
        print(current_path)
        return
    
    if col + 1 < m:
        find_paths(n, m, current_path + "r", row, col + 1)

    if row + 1 < n:
        find_paths(n, m, current_path + "d", row + 1, col)


n = int(input("Enter number of rows : "))
m = int(input("Enter number of columns : "))


find_paths(n, m)