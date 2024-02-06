n = int(input())
for i in range(1,n+1):
    print(int((i * i) * (i * i - 1) / 2 - (4 * (i - 2) * (i - 1))))