def hanoi(n, source, target, auxiliary):
    if n == 1:
        return 1
    else:
        count = 0
        count += hanoi(n - 1, source, auxiliary, target)
        count += 1
        count += hanoi(n - 1, auxiliary, target, source)
        return count
    
def step(n, source, target, auxiliary):
    if n == 1:
        print(source, target)
        
    else:
        count = 0
        count += step(n - 1, source, auxiliary, target)
        print(source, target)
        count += 1
        count += step(n - 1, auxiliary, target, source)
        

n = int(input())
print( hanoi(n, 1, 3, 2))

step(n, 1, 3, 2)
