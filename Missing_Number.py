def giveSum(array):
    sum = 0
    for i in array:
        sum += i
    return sum


totalSum = int(input())
other_4Nums = list(map(int, input().split()))
sum_of_3Num = giveSum(other_4Nums)
print(totalSum - sum_of_3Num)
