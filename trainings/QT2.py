h = int(input("Number of watermelons: "))
k = int(input("Number of melons: "))

life = (h*2) + k

if 0<=h<=100 and 0<=k<=100:

    if life == 0:
        print("YES")
    elif life % 2 == 0:
        print("YES")
    else:
        print("NO")

else:
    print("NO")