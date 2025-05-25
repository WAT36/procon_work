n=int(input())
s=input()
ans=0
ind=s.find("ABC")
while(ind!=-1):
    ans+=1
    ind=s.find("ABC",ind+1)
print(ans)
