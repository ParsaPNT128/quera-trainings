keyvoon = ["3", "3", "1", "1", "2", "2"]
nezam = ["1", "2", "3"]
shir_farhad = ["2", "1", "2", "3"]
all = [keyvoon, nezam, shir_farhad]

def score_calc(n , key):
    keyvoon_score = 0
    nezam_score = 0
    shir_farhad_score = 0
    for i in range(3):
        running = True
        while running:
            for j in range(len(all[i])):
                if len(all[i]) >= n:
                    running = False
                    break
                else:
                    all[i].append(all[i][j])

    keyvoon, nezam, shir_farhad = all
    for i in range(n):
        if keyvoon[i] == key[i]:
            keyvoon_score += 1
        if nezam[i] == key[i]:
            nezam_score += 1
        if shir_farhad[i] == key[i]:
            shir_farhad_score += 1

    top = max([keyvoon_score, nezam_score, shir_farhad_score])
    print(top)
    if keyvoon_score == top:
        print("keyvoon")
    if nezam_score == top:
        print("nezam")
    if shir_farhad_score == top:
        print("shir farhad")

n = int(input())
key = [*input()]

score_calc(n, key)