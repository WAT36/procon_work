h,w=map(int,input().split())

ans=9999999999999

#|-----|
#| | | |
#| | | |
#|-----|
if(w%3==0):
    ans=min(ans,0)
else:
    ans=min(ans,(((w//3)+1)*h)-((w//3)*h))


#|-----|
#|-----|
#|-----|
#|-----|
if(h%3==0):
    ans=min(ans,0)
else:
    ans=min(ans,(((h//3)+1)*w)-((h//3)*w))

#|-----| |-----|
#| |   | |   | |
#| |---| |---| |
#|-----| |-----|
if(h%2==0):
    for wi in range(1,w):
        a=(h//2)*wi
        b=(h//2)*wi
        c=h*(w-wi)
        ans=min(ans, max(a,b,c)-min(a,b,c))
else:
    for wi in range(1,w):
        a=(h//2)*wi
        b=((h//2)+1)*wi
        c=h*(w-wi)
        ans=min(ans, max(a,b,c)-min(a,b,c))


#|-----| |-----|
#|  |  | |-----|
#|-----| |  |  |
#|-----| |-----|
if(w%2==0):
    for hi in range(1,h):
        a=(w//2)*hi
        b=(w//2)*hi
        c=w*(h-hi)
        ans=min(ans, max(a,b,c)-min(a,b,c))
else:
    for hi in range(1,h):
        a=(w//2)*hi
        b=((w//2)+1)*hi
        c=w*(h-hi)
        ans=min(ans, max(a,b,c)-min(a,b,c))

print(ans)