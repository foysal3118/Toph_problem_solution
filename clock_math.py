hr, min = map(int, input().split())
hr_min = hr * 5
min_multy = float(5 / 60)
hr_to_12 = (60 - hr_min) - (min * min_multy)
total_angle = (hr_to_12 + min) * 6
if total_angle > 180:
    print(360 - total_angle)
else:
    print(total_angle)
