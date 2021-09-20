A, P = map(int, input().split())
dic={A:0}
before=A
ret=1
idx=1

def pow(a):
    if a==0: #종료 조건 명시
        return 0
    return (a%10)**P + pow(a//10)

while True:
    k=pow(before)
    if k not in dic:
        dic[k]=idx
        ret+=1
        idx+=1
        before=k
    else:
        ret=dic[k]
        break

print(ret)
