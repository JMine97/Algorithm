import sys
input=sys.stdin.readline

def GCD(a, b):
    if b==0:
        return a
    return GCD(b, a%b)

for _ in range(int(input())):
    a, b=map(int, input().split())

    div=GCD(b, a)

    result=div*(a//div)*(b//div)
    print(result)