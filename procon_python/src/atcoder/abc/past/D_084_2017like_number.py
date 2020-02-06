import bisect
prime_check=[True for i in range(100000)]
prime_check[0]=False
prime_check[1]=False

prime_num=[]

for i in range(2,100000):
    if(prime_check[i]):
        prime_num.append(i)
        for j in range(2*i,100000,i):
            prime_check[j]=False

like_num=[]
for pi in prime_num:
    if(prime_check[(pi+1)//2]):
        like_num.append(pi)

q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    l_ind=bisect.bisect_left(like_num, l)
    r_ind=bisect.bisect_right(like_num, r)
    print(r_ind - l_ind)
