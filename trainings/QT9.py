def dis_calc(n, a, m, o):
    common = []
    for i in range(min([n, m])):
        if a[i] == o[i]:
            common.append(a[i])
        else:
            for i in common:
                a.remove(i)
                o.remove(i)
                
            return len(a) + len(o)

n = int(input())
a = [*input()]
m = int(input())
o = [*input()]

print(dis_calc(n, a, m, o))