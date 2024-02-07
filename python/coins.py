t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    if a < b:
        a, b = b, a

    if a > 2 * b:
        print("NO")
    elif (a + b) % 3 == 0:
        print("YES")
    else:
        print("NO")