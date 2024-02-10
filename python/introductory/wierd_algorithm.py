i = int(input())
print(i,end=' ')
while(i>1):
    if(i%2 !=0):
        i = 3*i +1
        print(i, end =' ')
    else:
        i = i//2
        print(i, end=' ')