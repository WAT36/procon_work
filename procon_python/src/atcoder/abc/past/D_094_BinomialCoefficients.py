n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)

def mid(a):
    if(a%2!=0):
        return (a+1)//2
    else:
        return a//2

ai=a[0]
temp=list(map(lambda x:abs(x-mid(ai)),a[1:]))
bi=a[temp.index(min(temp))+1]
print(str(ai)+" "+str(bi))