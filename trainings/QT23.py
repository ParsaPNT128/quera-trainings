def func(s):
    answers = []
    a, b, c = list(map(int, s.split('?')))
    answers.append(a*b*c)
    answers.append(a*b+c)
    answers.append(a+b*c)
    answers.append(a+b+c)
    answers.append(a*(b+c))
    answers.append((a+b)*c)

    return max(answers)

print(func(input()))