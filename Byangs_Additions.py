firstNum, secondNum = map(list, input().split())
if len(firstNum) < len(secondNum):
    for j in range((len(secondNum) - len(firstNum))):
        firstNum.insert(0, "0")
elif len(secondNum) < len(firstNum):
    for k in range((len(firstNum) - len(secondNum))):
        secondNum.insert(0, "0")
for i in range(len(firstNum)):
    if int(secondNum[i]) + int(firstNum[i]) >= 10:
        print("Yes")
        break
if int(secondNum[i]) + int(firstNum[i]) < 10:
    print("No")
