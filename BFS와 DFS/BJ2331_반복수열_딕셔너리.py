A, P = map(int, input().split())
dic={A:0}
before=A
ret=1
idx=1
while True:
    k=0
    for a in str(before):
        k+=int(a)**P
    if k not in dic:
        dic[k]=idx
        ret+=1
        idx+=1
        before=k
    else:
        ret=dic[k]
        break

print(ret)
