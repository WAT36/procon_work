n,k=map(int,input().split())
a=0
for i in range(n):
    a+=int(input())
    if(a>=k):
        print(i+1)
        break
