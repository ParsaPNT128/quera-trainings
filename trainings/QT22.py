def func(string):
    c = 0
    nstring = ''
    r = 11 - int(string[len(string)-1])
    if r == 10:
        return "it's not unique!"

    for i, s in enumerate(string):
        if s == '?':
            multi = 11 - (i+1)

    for i, s in enumerate(string):
        if 11-(i+1) != multi and 11-(i+1) != 1:
            c += int(s) * (11-(i+1))

    for i in range(10):
        if (c + (i*multi)) % 11 == r:
            for letter in string:
                if letter == '?':
                    nstring += str(i)
                else:
                    nstring += letter

            return nstring

    return 'cannot be recovered!'

answers = []
for i in range(int(input())):
    answers.append(func(input()))

for i in answers:
    print(i)