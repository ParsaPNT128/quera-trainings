def play(move):
    global player, hand
    if move[0] == "1":
        if move[1] == player:
            if hand == "L":
                hand = "R"
            else:
                hand = "L"
    else:
        if move[1] == player and move[2] == hand:
            player = str(int(player) + 1)
            hand = move[3]
        elif player == str(int(move[1]) + 1) and move[3] == hand:
            player = str(int(player) - 1)
            hand = move[2]

n = int(input())
player, hand = input().split()

for i in range(n):
    play(input().split())

print(player, hand)