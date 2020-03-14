n,k=map(int,input().split())
t=[]
t.append(int(input()))
t.append(int(input()))
now_sleep=t[0]+t[1]
for i in range(2,n):
    ti=int(input())
    now_sleep+=ti
    t.append(ti)
    if(now_sleep<k):
        print(i+1)
        break
    now_sleep-=t[-3]
else:
    print(-1)
