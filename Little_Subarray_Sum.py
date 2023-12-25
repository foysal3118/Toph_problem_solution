totalNum, st, end = map(int, input().split())
arry = list(map(int, input().split()))
sum = 0
for i in range(st, end + 1):
    sum = sum + arry[i]
print(sum)
