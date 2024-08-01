answers = []
messages = ['Peygir', 'Tannaz']
n = 1

def message_tracker(k, messages):
    if k == len(messages):
        return messages[k - 1]
    
    minus = int(k / len(messages))
    k = k - minus * len(messages)
    return messages[k - 1]


q, t = input().split()

for i in range(int(t)*3-1):
    if messages[len(messages) - 1] == 'Morshed':
        if n != int(t):
            messages.append('Tannaz')
        else:
            messages.append('Peygir')
            messages.append('Tannaz')
            n = 0
    elif messages[len(messages) - 1] == 'Tannaz':
        if n != t:
            messages.append('Jeddy')
        else:
            messages.append('Peygir')
            messages.append('Jeddy')
            n = 0
    elif messages[len(messages) - 1] == 'Jeddy':
        if n != t:
            messages.append('Morshed')
        else:
            messages.append('Peygir')
            messages.append('Morshed')
            n = 0

    n += 1

for i in range(int(q)):
    k = int(input())
    answers.append(message_tracker(k , messages))

for i in answers:
    print(i)