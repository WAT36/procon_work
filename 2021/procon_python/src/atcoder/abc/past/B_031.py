l,h=map(int,input().split())
n=int(input())
for i in range(n):
    ai=int(input())
    if(ai<l):
        print(l-ai)
    elif(h<ai):
        print(-1)
    else:
        print(0)
