def run_cinema(k, friends):
    people = [int(i)+1 for i in friends]
    while True:
        if sum(people) <= int(k):
            return len(people)
        else:
            people.remove(max(people))

n, k = input().split()
friends = input().split()

print(run_cinema(k, friends))