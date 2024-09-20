cities = {
    1: [2, 3, 4],
    2: [1, 3, 4, 5, 6],
    3: [1, 2, 4, 6, 7],
    4: [1, 2, 3, 5, 6, 7],
    5: [2, 4, 6],
    6: [2, 3, 4, 5, 7],
    7: [3, 4, 6]
}

def play(c, r):
    day = 0
    running = True
    while running:
        if r in cities[c]:
            running = False
            day += 1
            return day
        else:
            r = [i for i in cities[r] if i in cities[c]][0]
            c = [i for i in cities[r] if i not in cities[c]][0]
            day += 1

c = int(input())
r = int(input())

print(play(c, r))