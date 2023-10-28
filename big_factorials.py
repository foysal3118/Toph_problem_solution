Num = int(input())
factorial = 1
for i in range(2, Num + 1, 1):
    factorial = factorial * i
lenthFactorNum = len(str(factorial))
strNum = str(factorial)
reverseResult = strNum[-1:-5:-1]
if lenthFactorNum <= 4:
    print(factorial)
else:
    print(reverseResult[::-1])
