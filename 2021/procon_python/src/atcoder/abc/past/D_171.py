import collections

def list_count(l):
    return collections.Counter(l)


n=int(input())
a=list(map(int,input().split()))
a_val_list=list_count(a)
a_sum=sum(a)

q=int(input())

for i in range(q):
    b,c=map(int,input().split())
    b_val=a_val_list.get(b, 0)
    a_val_list[b]=0
    a_sum-=b*b_val

    a_val_list[c]=a_val_list.get(c,0)+b_val
    a_sum+=c*b_val

    print(a_sum)


