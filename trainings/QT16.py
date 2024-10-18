def func(n, a):
    down = False
    up = False
    if a[1] > a[0]:
        for i in range(1, n):
            if a[i] > a[i-1]:
                if down:
                    return "No"
            elif a[i] < a[i-1]:
                down = True
    elif a[1] < a[0]:
        for i in range(1, n):
            if a[i] < a[i-1]:
                if up:
                    return "No"
            elif a[i] > a[i-1]:
                up = True

    return "Yes"

n = int(input())
a = input().split()

for i, num in enumerate(a):
    a[i] = int(num)

print(func(n, a))
