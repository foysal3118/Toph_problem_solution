hr, min = [int(i) for i in input().split()]
# space_cal;
min_space_from_12_to_CW = min
hr_space_from_12_to_acw = 60 - (hr * 5)
# 1 min = 5/60 space
hr_space_decrese_to_min = hr_space_from_12_to_acw - (min * (5 / 60))
# degree_cal;
min_degree_from_12 = min_space_from_12_to_CW * 6  # 1 space = 6 degree
hr_degree_from_12 = hr_space_decrese_to_min * 6
total_degree = min_degree_from_12 + hr_degree_from_12
if total_degree > 180:
    total_degree = 360 - total_degree
print(total_degree)
