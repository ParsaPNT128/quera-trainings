def stones_calc(stones, dropped):
    counting = False
    count = 0
    for i in stones:
        if counting: 
            count += 1
        if int(i) == dropped:
            counting = True
            if i != stones[0]:
                count += 1

    return count

stones = input().split()
dropped = int(input())

print(stones_calc(stones, dropped))