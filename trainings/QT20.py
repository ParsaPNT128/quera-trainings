def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def func(houses, s, t):
    o = 0
    k = 0
    for i in range(min([s, t]), max([s, t])):
        if houses[i] == "H" and houses[i-1] != "H":
            k += 1
        elif houses[i] == "H":
            k += 1
        elif k != 0:
            if is_power_of_two(k):
                o += 1
            k = 0

    return o

n = int(input())
houses = input()
s, t = input().split()

print(func(houses, int(s), int(t)))