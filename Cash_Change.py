x = [500, 100, 50, 10, 5, 1]
n = int(input())
a = []
for i in x:
    while n >= i:
        a.append(i)
        n = n - i
print(*sorted(a))
