import bisect
n,k=map(int,input().split())
s=[0 for _ in range((10**5)+1)]
maxa=0
for i in range(n):
    a,b=map(int,input().split())
    s[a]+=b
    maxa=max(maxa,a)
s=s[:maxa]
#print(s)
for i in range(1,len(s)):
    s[i]+=s[i-1]
#print(s)
print(bisect.bisect_left(s, k))