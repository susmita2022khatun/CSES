n= int(input())
array = [int(i) for i in input().split()]
result = 0
for i in range(n-1):
    if array[i]> array[i+1]:
        result = result+ array[i]-array[i+1]
        array[i+1] = array[i]
print(result, end=' ')