first, last = map(int, input().split())
num1 = 0
num2 = 1
cur_num = 0
while cur_num <= last:
    if first <= cur_num <= last:
        print(cur_num)
    cur_num = num2 + num1
    num1 = num2
    num2 = cur_num
