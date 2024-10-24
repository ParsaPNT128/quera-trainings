from math import ceil

def find_squares(n):
    squares = 0
    for i in range(1, ceil(n / 2) + 1):
        x = i * i
        for l in range(1, ceil(n / 2) + 1):
            y = l * l
            if abs(x - y) == n:
                squares += 1

    return int(squares / 2)

outputs = []
t = int(input())
for i in range(t):
    outputs.append(find_squares(int(input())))

for i in outputs:
    print(i)