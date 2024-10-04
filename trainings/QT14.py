from math import factorial

def calculate(n):
    for i in range(n):
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()
        
n = int(input())
calculate(n)