def game(key, guess):
    global game_over
    output = ""
    repeated = []

    if game_over:
        return "Game Over"
    elif len(key) != len(guess):
        return "Invalid Length"
    else:
        for i in range(len(guess)):
            if guess[i] == key[i]:
                output += "G"
                repeated.append(guess[i])
            elif guess[i] in key:
                if not guess[i] in repeated:
                    output += "Y"
                    repeated.append(guess[i])
                else:
                    output += "R"
            else:
                output += "R"

    if not "Y" in output and not "R" in output:
        game_over = True

    return output
        
game_over = False
outputs = []
key = input()
ng = int(input())
for i in range(ng):
    outputs.append(game(key, input()))

for i in outputs:
    print(i)