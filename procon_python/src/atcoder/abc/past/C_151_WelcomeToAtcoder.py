n,m=map(int,input().split())
wa_check=[0 for _ in range(n+1)]
ac_check=[0 for _ in range(n+1)]
for i in range(m):
    p,s=input().split()
    p=int(p)
    if(ac_check[p]==0):
        if(s=='AC'):
            ac_check[p]=1
        else:
            wa_check[p]+=1
wa_ans=[wa_check[i] for i in range(n+1) if ac_check[i]!=0]
print(sum(ac_check),sum(wa_ans))

# wa=0
# ac=0
# ac_check=[0 for _ in range(n+1)]
# for i in range(m):
#     p,s=input().split()
#     p=int(p)
#     if(ac_check[p]==0):
#         if(s=="AC"):
#             ac+=1
#             ac_check[p]=1
#         else:
#             wa+=1
# print(ac,wa)

