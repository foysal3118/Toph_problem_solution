all_xy_value = []
last_result = float("inf")
# This version initializes last_result with positive infinity
# ensuring that any valid distance will be smaller than the initial value.
# for maximum I can aso use float('-inf')
for i in range(int(input())):
    xy_value = list(map(int, input().split()))
    if i == 0:
        all_xy_value.append(xy_value)
    else:
        for k in range(i):
            x_in_arry, y_in_arry = all_xy_value[k]
            cur_x, cur_y = xy_value
            cur_result = float(
                (((cur_x - x_in_arry) ** 2) + ((cur_y - y_in_arry) ** 2)) ** 0.5
            )
            if cur_result < last_result:
                last_result = cur_result
        all_xy_value.append(xy_value)
print(last_result)
