h,w=map(int,input().split())
a=[]
for i in range(h):
    a.extend(list(input()))

if(h%2==0 and w%2==0):
    set_a=list(set(a))
    for set_ai in set_a:
        set_ai_count=a.count(set_ai)
        if(set_ai_count%4 != 0):
            print('No')
            break
    else:
        print('Yes')

elif(h%2==0):
    set_a=list(set(a))
    two_mul_count=0
    for set_ai in set_a:
        set_ai_count=a.count(set_ai)
        if(set_ai_count%4 == 0):
            continue
        elif(set_ai_count%2 == 0):
            two_mul_count+=1
        else:
            print('No')
            break
    else:
        if(two_mul_count<=(h//2)):
            print('Yes')
        else:
            print('No')

elif(w%2==0):
    set_a=list(set(a))
    two_mul_count=0
    for set_ai in set_a:
        set_ai_count=a.count(set_ai)
        if(set_ai_count%4 == 0):
            continue
        elif(set_ai_count%2 == 0):
            two_mul_count+=1
        else:
            print('No')
            break
    else:
        if(two_mul_count<=(w//2)):
            print('Yes')
        else:
            print('No')

else:
    set_a=list(set(a))
    two_mul_count=0
    odd_count=0
    for set_ai in set_a:
        set_ai_count=a.count(set_ai)
        if(set_ai_count%4 == 0):
            continue
        elif(set_ai_count%2 == 0):
            two_mul_count+=1
        else:
            odd_count+=1
    else:
        if(odd_count>1):
            print('No')
        elif(two_mul_count<=(w//2)+(h//2)):
            print('Yes')
        else:
            print('No')

