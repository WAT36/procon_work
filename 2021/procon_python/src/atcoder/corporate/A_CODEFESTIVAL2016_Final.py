h,w=map(int,input().split())
s=[]
alpha=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(h):
    si=list(input().split())
    if('snuke' in si):
        print(alpha[si.index('snuke')]+str(i+1))
        break
