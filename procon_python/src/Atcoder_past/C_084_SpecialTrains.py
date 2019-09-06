n=int(input())
c=[]
s=[]
f=[]
for i in range(n-1):
    ci,si,fi=map(int,input().split())
    c.append(ci)
    s.append(si)
    f.append(fi)
for h in range(n):
    now=0
    for i in range(h,n-1):
        if(now <= s[i]):
            now = s[i]+c[i]
        else:
            now =  s[i] + (-(-(now-s[i])//f[i]))*f[i] + c[i]
#        print("i:"+str(i)+" now:"+str(now))
    print(now)