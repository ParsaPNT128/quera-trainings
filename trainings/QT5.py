answers = []
# bar = 2
# n = 2
# akharin 
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
                n = 1
        elif messages[len(messages) - 1] == 'Tannaz':
            if n != t:
                messages.append('Jeddy')
            else:
                messages.append('Peygir')
                messages.append('Jeddy')
                n = 1
        elif messages[len(messages) - 1] == 'Jeddy':
            if n != t:
                messages.append('Morshed')
            else:
                messages.append('Peygir')
                messages.append('Morshed')
                n = 1

        n += 1
    
    return messages[k -1]
    
    

q, t = input().split()
for i in range(int(q)):
    k = int(input())
    answers.append(message_tracker(k , int(t)))

for i in answers:
    print(i)