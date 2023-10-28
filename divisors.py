n = int(input())
divisor = []
for i in range(1, n + 1):
    if n % i == 0:
        initial_div = n // i
        if initial_div not in divisor:
            divisor.append(initial_div)
            if i not in divisor:
                divisor.append(i)
divisor.sort()
for j in divisor:
    print(j)
