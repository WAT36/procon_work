s=input()
q=int(input())
is_reverse=False
pre=[]
post=[]
for i in range(q):
    qi=list(input().split())
    if(len(qi)==1):
        is_reverse = not is_reverse
    elif(qi[1]=="1"):
        if(is_reverse):
            post.append(qi[2])
        else:
            pre.append(qi[2])
    else:
        if(is_reverse):
            pre.append(qi[2])
        else:
            post.append(qi[2])

if(is_reverse):
    print(''.join(post)[::-1] + s[::-1] + ''.join(pre))
else:
    print(''.join(pre)[::-1] + s + ''.join(post))