n=int(input())
alist=[]

for i in range(n):
    ai=int(input())
    alist.append(ai)
aset=set(alist)
print(len(alist) - len(aset))
