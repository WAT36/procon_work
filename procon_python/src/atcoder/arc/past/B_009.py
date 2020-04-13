num_order={}
num_reverse={}
b=list(map(int,input().split()))

for i in range(10):
    num_order[str(b[i])]=str(i)
    num_reverse[str(i)]=str(b[i])

n=int(input())
a=[]

for i in range(n):
    ai=input()
    ai_ordered=[]
    for aij in ai:
        ai_ordered.append(num_order[aij])
    a.append(int(''.join(ai_ordered)))

a.sort()
#print(a)
for i in range(len(a)):
    ai=a[i]
    ai_ordered=[]
    for aij in str(ai):
        ai_ordered.append(num_reverse[str(aij)])
    print(''.join(ai_ordered))