step = int(input())
num1 = 1
num2 = 1
series = [1, 1]
for i in range(3, (step + 1), 1):
    finalNum = num1 + num2
    series.append(finalNum)
    num1 = num2
    num2 = finalNum
print(series[step - 1])
