n = input()
m = str(n)
nList = list(m)
if len(m) <= 3:
    print(n)
elif len(m) % 3 == 0:
    for i in range((len(m) // 3) + 1):
        nList = []
        finalOutput = ""
