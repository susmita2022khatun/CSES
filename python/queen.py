
def rec(j):
    global c
    if j == 8:
        c += 1
        return
    for i in range(8):
        if chess[i][j] == '.' and not ld[i - j + 7] and not rd[i + j] and not row[i]:
            ld[i - j + 7] = True
            rd[i + j] = True
            row[i] = True
            rec(j + 1)
            ld[i - j + 7] = False
            rd[i + j] = False
            row[i] = False


chess = [list(input()) for _ in range(8)]
c = 0
ld = [False] * 15
rd = [False] * 15
row = [False] * 8
rec(0)
print(c)