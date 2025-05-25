import fractions
import sys
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

if(k in a):
    print("POSSIBLE")
    sys.exit()

maxa=max(a)
mindiff=a[0]
for i in range(len(a)-1):
    mindiff=fractions.gcd(mindiff,a[i])

a_more_k=[a[i] for i in range(len(a)) if a[i]>k]
for i in range(len(a_more_k)):
    if( (a_more_k[i]-k)%mindiff == 0):
        print("POSSIBLE")
        sys.exit()

print("IMPOSSIBLE")

