import collections

n,c=map(int,input().split())
a_even=[]
a_odd=[]
for i in range(n):
    ai=int(input())
    if(i%2==0):
        a_even.append(ai)
    else:
        a_odd.append(ai)


aec=collections.Counter(a_even)
ae1=-1
ae1_num=0
for k,v in aec.items():
    if(ae1_num<v):
        ae1_num=v
        ae1=k

aec.pop(ae1)

ae2=-1
ae2_num=0
for k,v in aec.items():
    if(ae2_num<v):
        ae2_num=v
        ae2=k


aoc=collections.Counter(a_odd)
ao1=-1
ao1_num=0
for k,v in aoc.items():
    if(ao1_num<v):
        ao1_num=v
        ao1=k

aoc.pop(ao1)

ao2=-1
ao2_num=0
for k,v in aoc.items():
    if(ao2_num<v):
        ao2_num=v
        ao2=k

#print(ae1,ae1_num,ae2,ae2_num)
#print(ao1,ao1_num,ao2,ao2_num)
if(ae1 != ao1):
    print(((len(a_even)-ae1_num) + (len(a_odd)-ao1_num))*c)
else:

    print(min( ((len(a_even)-ae1_num) + (len(a_odd)-ao2_num))*c,
               ((len(a_even)-ae2_num) + (len(a_odd)-ao1_num))*c ))

