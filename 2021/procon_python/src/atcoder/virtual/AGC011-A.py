n,c,k=map(int,input().split())
t=[]
for i in range(n):
    t.append(int(input()))
t.sort()

bus=0
wait_p=0
first_t=-1

for i in range(n):
    ti=t[i]
    if(first_t==-1):
        first_t=ti

    wait_p+=1

    if(ti > first_t+k):
        bus+=1
        first_t=ti
        wait_p=1

    if(wait_p >= c):
        bus+=1
        first_t=-1
        wait_p=0


if(first_t!=-1 or wait_p > 0):
    bus+=1

print(bus)
