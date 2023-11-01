firstNum, secondNum = map(list, input().split())
if len(firstNum) < len(secondNum):
    for j in range(0, (len(secondNum) - len(firstNum))):
        firstNum.insert(0, "0")
elif len(secondNum) < len(firstNum):
    for k in range(0, (len(firstNum) - len(secondNum))):
        secondNum.insert(0, "0")
for i in range(0, len(firstNum)):
    if int(secondNum[i]) + int(firstNum[i]) >= 10:
        print("Yes")
        break
if int(secondNum[i]) + int(firstNum[i]) < 10:
    print("No")
