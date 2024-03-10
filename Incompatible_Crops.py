array = []
r, c = map(int, input().split())
for i in range(r):
    line = input()
    sub_array = list(line)
    array.append(sub_array)
count = 0
for i in range(r):
    if i == 0:  # first sub array
        for j in range(c):
            if j == 0:
                if (
                    (array[i][j] == ".")
                    and (array[i][j + 1] == ".")
                    and (array[i + 1][j] == ".")
                ):
                    count += 1
            elif j == c - 1:
                if (
                    (array[i][j] == ".")
                    and (array[i][j - 1] == ".")
                    and (array[i + 1][j] == ".")
                ):
                    count += 1
            else:
                if (
                    (array[i][j] == ".")
                    and (array[i][j - 1] == ".")
                    and (array[i][j + 1] == ".")
                    and (array[i + 1][j] == ".")
                ):  # possition check
                    count += 1
    elif i == r - 1:  # last sub array
        for j in range(c):
            if j == 0:
                if (
                    (array[i][j] == ".")
                    and (array[i][j + 1] == ".")
                    and (array[i - 1][j] == ".")
                ):
                    count += 1
            elif j == c - 1:
                if (
                    (array[i][j] == ".")
                    and (array[i][j - 1] == ".")
                    and (array[i - 1][j] == ".")
                ):
                    count += 1
            else:
                if (
                    (array[i][j] == ".")
                    and (array[i][j - 1] == ".")
                    and (array[i][j + 1] == ".")
                    and (array[i - 1][j] == ".")
                ):  # possition check
                    count += 1

    else:  # middle sub array
        for j in range(c):
            if j == 0:
                if (
                    (array[i][j] == ".")
                    and (array[i][j + 1] == ".")
                    and (array[i - 1][j] == ".")
                    and (array[i + 1][j] == ".")
                ):
                    count += 1
            elif j == c - 1:
                if (
                    (array[i][j] == ".")
                    and (array[i][j - 1] == ".")
                    and (array[i - 1][j] == ".")
                    and (array[i + 1][j] == ".")
                ):
                    count += 1
            else:
                if (
                    (array[i][j] == ".")
                    and (array[i][j - 1] == ".")
                    and (array[i][j + 1] == ".")
                    and (array[i - 1][j] == ".")
                    and (array[i + 1][j] == ".")
                ):  # possition check
                    count += 1
print(count)
