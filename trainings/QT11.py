def calc(n, m):
    if n == m:
        return n + 1
    else:
        return max([n, m])

answers = []
t = int(input())
for i in range(t):
    n, m = input().split()
    answers.append(calc(int(n), int(m)))

for i in answers:
    print(i)