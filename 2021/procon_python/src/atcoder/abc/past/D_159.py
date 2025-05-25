import collections
n=int(input())
a=list(map(int,input().split()))

a_count=collections.Counter(a)

nctwo=[0,0,1]

def nc2(i):
    if(len(nctwo)>i):
        return nctwo[i]
    else:
        while(len(nctwo)<=i):
            nctwo.append(nctwo[-1] * len(nctwo) / (len(nctwo)-2))
        return nctwo[i]

allsum=0
for v in a_count.values():
    allsum+=nc2(v)

for i in range(n):
    ai_count=a_count[a[i]]
    print(int(allsum-(nc2(ai_count) - nc2(ai_count-1))))
