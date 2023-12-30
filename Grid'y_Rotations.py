main_arry = []
m, n = map(int, input().split())
for i in range(m):
    main_arry.append(list(map(int, input().split())))
for j in range(int(input())):
    r, c = map(int, input().split())
    # firstly removing last part andd adding to next line
    first_line_out = main_arry[r - 1].pop(c + 1)
    second_line_out = main_arry[r].pop(c + 1)
    main_arry[r].insert(c + 1, first_line_out)
    main_arry[r + 1].insert(c + 2, second_line_out)
    # now adding to starting value to previous line
    last_line_out = main_arry[r + 1].pop(c - 1)
    main_arry[r].insert(c - 1, last_line_out)
    second_line_out = main_arry[r].pop(c)
    main_arry[r - 1].insert(c - 1, second_line_out)
    for k in main_arry:
        print(*k)
