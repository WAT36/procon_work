a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())

if(w>=v):
    print('NO')
else:
    ans=abs(a-b)/abs(v-w)
    if(ans>t):
        print('NO')
    else:
        print('YES')
