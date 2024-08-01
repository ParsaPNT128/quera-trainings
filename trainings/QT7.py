winners = []

def winner_calc(points):
    c = 0
    q = 0

    for i in points:
        if i == 'C':
            c += 1
        else:
            q += 1

    if c > q:
        winners.append('CodeCup')
    else:
        winners.append('Quera')

t = int(input())
for i in range(t):
    n = int(input())
    points = [*input()]
    winner_calc(points)

for i in winners:
    print(i)