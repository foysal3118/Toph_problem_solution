def count1s(value):
    value = str(bin(value))
    count = 0
    for i in value:
        if i == "1":
            count += 1
    return count


input_num = int(input())
num_of_1s = count1s(input_num)
total_1s = "1" * num_of_1s
print(int(total_1s, 2))
