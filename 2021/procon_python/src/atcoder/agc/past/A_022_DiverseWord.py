s=input()
ans=""

slist=list(s)
if(len(slist)==26):
    if(s=='zyxwvutsrqponmlkjihgfedcba'):
        print(-1)
    else:
        tlist=list(s)
        while(''.join(tlist)!='zyxwvutsrqponmlkjihgfedcba'):
            ttail=tlist.pop(-1)
            while(ttail=='z'):
                ttail=tlist.pop(-1)
            tlist.append(chr(ord(ttail)+1))

            if(len(tlist) == len(list(set(tlist)))):
                break

        print(''.join(tlist))
else:
    tlist=list(s)
    tlist.append('a')
    c=97
    while(ord('z') >= c):
        tlist[-1]=chr(c)
        if(len(list(set(slist))) != len(list(set(tlist)))):
            break
        else:
            c+=1
    print(''.join(tlist))