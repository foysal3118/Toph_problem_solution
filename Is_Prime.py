n = int(input())
for i in range(2, 10):
    if i == n:
        c = 0
    elif n % i == 0:
        print("No")
        break
if i == 9:
    print("Yes")
