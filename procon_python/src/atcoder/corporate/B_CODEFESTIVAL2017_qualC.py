import copy
n=int(input())
a=list(map(int,input().split()))

aa=[a]
ans=set([])
for i in range(n):
    ai=[]
    for aai in aa:
        aaij=copy.deepcopy(aai)
        aaij[i]-=1
        ansi=1
        for j in range(len(aaij)):
            ansi*=aaij[j]
        if(ansi%2==0):
            ans.add('-'.join(list(map(str,aaij))))
        ai.append(aaij)

        aaij=copy.deepcopy(aai)
        ansi=1
        for j in range(len(aaij)):
            ansi*=aaij[j]
        if(ansi%2==0):
            ans.add('-'.join(list(map(str,aaij))))
        ai.append(aaij)

        aaij=copy.deepcopy(aai)
        aaij[i]+=1
        ansi=1
        for j in range(len(aaij)):
            ansi*=aaij[j]
        if(ansi%2==0):
            ans.add('-'.join(list(map(str,aaij))))
        ai.append(aaij)
    aa=ai

print(len(ans))