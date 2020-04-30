n=int(input())
s=[]
for _ in range(n):
    si=int(input())
    if(si!=0):
        s.append(si)
s.sort(reverse=True)

q=int(input())
for _ in range(q):
    ki=int(input())
    if(ki>=len(s)):
        print(0)
    else:
        print(s[ki]+1)
