def coin_combinations(n):
    for c500 in range(n // 500 + 1):
        for c100 in range((n - c500 * 500) // 100 + 1):
            for c10 in range((n - c500 * 500 - c100 * 100) // 10 + 1):
                for c5 in range((n - c500 * 500 - c100 * 100 - c10 * 10) // 5 + 1):
                    c1 = n - (c500 * 500 + c100 * 100 + c10 * 10 + c5 * 5)
                    if c1 >= 0 and c500 * 500 + c100 * 100 + c10 * 10 + c5 * 5 + c1 == n:
                        print(f"500: {c500} 100: {c100} 10: {c10} 5: {c5} 1: {c1}")

n = int(input("Enter n : "))
print(f"500: {0} 100: {0} 10: {0} 5: {0} 1: {0}")
coin_combinations(n)