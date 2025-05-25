n=int(input())
s=input()
nt=n//2
if(s[:nt] ==s[nt:]):
    print("Yes")
else:
    print("No")