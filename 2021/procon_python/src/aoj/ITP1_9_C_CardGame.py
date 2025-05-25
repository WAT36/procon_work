n=int(input())
taro=0
hanako=0
for i in range(n):
    c=list(input().split())
    if(c[0] < c[1]):
        hanako+=3
    elif(c[0] > c[1]):
        taro+=3
    else:
        taro+=1
        hanako+=1
print("{0} {1}".format(taro,hanako))
