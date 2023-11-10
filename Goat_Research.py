arry = []
for i in range(int(input())):
    n = input()
    if n.count("a") % 2 != 0 and n.count("a") > 1:
        arry.append(n[0 : len(n) - 1])
    elif n.count("a") == 1:
        arry.append(n + "a")
    else:
        arry.append(n)
max = len(max(arry))
for j in arry:
    space = " " * ((max - len(j)) // 2)
    print(f"{space}{j}")
