b = int(input())
s = 1
for i in range(2, b + 1):
    s = s * i
n = str(s)
a = n[-1:-5:-1]
print(a[::-1])
