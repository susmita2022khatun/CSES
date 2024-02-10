t = int(input())

for _ in range(t):
    n = int(input())
    charges = list(map(int, input().split()))
    
    pointer = 0
    charges_used = 0

    while pointer < n:
        max_range = 0
        chosen_charge = None

        for i in range(pointer, min(pointer + charges[pointer], n)):
            if i + charges[i] - 1 >= max_range:
                max_range = i + charges[i] - 1
                chosen_charge = i

        pointer = max_range + 1
        charges_used += 1

    print(charges_used)
