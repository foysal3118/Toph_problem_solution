n = int(input())
arry = ""
for i in range(3, 0, -1):
    avgtrip = n // i
    trip = n - avgtrip
    n = trip
    if i == 0:
        arry = arry + str(avgtrip)
    if i != 0:
        arry = arry + str(avgtrip) + " "
print(arry)
