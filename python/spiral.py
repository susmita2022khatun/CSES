a = int(input())

for i in range(a):
    y, x = map(int, input().split())

    if y > x:
        if y % 2:
            ans = (y - 1) ** 2 + x
        else:
            ans = y ** 2 - x + 1
    else:
        if x % 2:
            ans = x ** 2 - y + 1
        else:
            ans = (x - 1) ** 2 + y

    print(ans)