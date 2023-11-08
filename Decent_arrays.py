lenth = int(input())
arry = list(map(int, input().split()))
max = arry[0]
for i in range(1, lenth):
    if max <= arry[i]:
        max = arry[i]
        continue
    else:
        print("No")
        break
if max <= arry[i]:
    print("Yes")
