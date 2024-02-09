n = int(input())

weights = list(map(int, input().split()))
def diff(index, a, b):
    if index >= len(weights):
        return abs(a - b)
    return min(diff(index + 1, a + weights[index], b), diff(index + 1, a, b + weights[index]))
print(diff(0, 0, 0))