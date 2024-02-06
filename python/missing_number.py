n= int(input())

main = n*(n+1)//2 - sum(int(i) for i in input().split())
print(main, end=' ')