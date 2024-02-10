a = str(input()).upper()
maximum = 0
count = 0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count = count+1
        maximum = max(count, maximum)
    elif a[i]!=a[i+1]:
        count = 0
print(maximum+1, end=' ')