def find_complement(hex_code):
    rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    n1, n2, n3 = 255, 255, 255
    
    for x, i in enumerate(rgb):
        if x == 0:
            n1 -= i
        elif x == 1:
            n2 -= i
        else:
            n3 -= i

    rgb_code = (n1, n2, n3)
    hexa = '#%02x%02x%02x' % rgb_code

    return hexa.upper()

results = []
t = int(input())
for i in range(t):
    hex_code = input().lstrip('#')
    results.append(find_complement(hex_code))

for i in results:
    print(i)