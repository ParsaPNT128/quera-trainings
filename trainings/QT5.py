answers = []
k = []

def message_tracker(k, t):
    messages = ['Peygir', 'Tannaz']
    n = 1
    for i in range(k):
        if messages[len(messages) - 1] == 'Morshed':
            if n != t:
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
    
    return messages
    
q, t = input().split()
for i in range(int(q)):
    k.append(int(input()))

messages = message_tracker(max(k) , int(t))

for i in k:
    answers.append(messages[i - 1]) 

for i in answers:
    print(i)