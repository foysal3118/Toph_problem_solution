main_line = list(map(str, input().split()))
for i in range(len(main_line) - 1, -1, -1):
    if main_line[i].upper() == main_line[i]:
        main_line.pop(i)
for word in main_line:
    print(word, end=" ")
