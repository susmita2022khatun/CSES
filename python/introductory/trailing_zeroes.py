n = int(input())

ans = 0
current = 5
while(current<=n):
    ans = ans + int(n/current)
    current = current*5
print(ans)