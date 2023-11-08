num = input()
max = -1
for i in range(10):
    if num.count(str(i)) > max:
        max = num.count(str(i))
        out = i
print(out)
