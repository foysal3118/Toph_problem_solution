arry = "abcdefghijklmnopqrstuvwxyz"
shift = int(input())
text = list(input())
for i in range(len(text)):
    if text[i] == " ":
        continue
    else:
        pos = arry.index(text[i])
        text.pop(i)
        text.insert(i, arry[pos - shift])
for j in text:
    print(j, end="")
