n,t=map(int,input().split())
tici=[]
for i in range(n):
    ci,ti=map(int,input().split())
    if(ti<=t):
        tici.append([ci,ti])
if(len(tici)==0):
    print('TLE')
else:
    tici.sort()
    print(tici[0][0])
