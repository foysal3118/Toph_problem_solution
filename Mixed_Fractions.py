numerator, denominator = map(int, input().split())
whole_num = numerator // denominator
new_numerator = numerator % denominator
print(whole_num, new_numerator, denominator)
