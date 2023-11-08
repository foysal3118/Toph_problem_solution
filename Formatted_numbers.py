num = list(input())
for i in range(len(num) - 3, -1, -3):
    if i <= 0:
        break
    else:
        num.insert(i, ",")
for j in num:
    print(j, end="")
