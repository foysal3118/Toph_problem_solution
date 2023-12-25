a = str(input()).lower()
b = str(input()).lower()
A = list(a)
B = list(b)
if len(a) == len(b):
    x = 0
    for i in range(0, len(a) - 1):
        x = x + 1
    if A[x] not in B:
        print("No")
    else:
        print("Yes")
else:
    print("No")
