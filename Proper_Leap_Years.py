x = int(input())
if (x % 4) == 0 and (x % 100) == 0 and (x % 400) == 0:
    print("Yes")
elif (x % 4) == 0 and (x % 100) == 0 and (x % 400) != 0:
    print("No")
elif (x % 4) != 0:
    print("No")
elif (x % 4) == 0 and x % 100 != 0:
    print("Yes")
