from math import ceil

def time_calc(k, n, h):
    time = n
    h = [0] + h + [0]
    for i in range(1, n+2):
        b1 = int(h[i])
        b2 = int(h[i-1])
        dis = abs(b1 - b2)
        time += ceil(dis / k)

    return time

k = int(input())
n = int(input())
h = (input()).split()

print(time_calc(k, n, h))