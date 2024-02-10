t = int(input())

def position(position):
    block_size = 9
    num_digits = 1
    while position > block_size * num_digits:
        position -= block_size * num_digits
        block_size *= 10
        num_digits += 1

    num = (position - 1) // num_digits + 10 ** (num_digits - 1)

    digit_position = (position - 1) % num_digits

    return int(str(num)[digit_position])

for _ in range(t):
    n = int(input())
    print(position(n))
