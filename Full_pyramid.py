n = int(input())
for i in range(1, n + 1):
    first_space = " " * (n - i)
    print(first_space + "*", end="")
    for j in range(i - 1):
        print(" " + "*", end="")
    print()
