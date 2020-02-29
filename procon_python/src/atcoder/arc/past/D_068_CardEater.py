n=int(input())
a=list(map(int,input().split()))
# num={}
# for ai in a:
#     num_ai=num.get(ai, 0)
#     num[ai]=num_ai+1

# even=0
# odd=0
# for k,v in num.items():
#     if(v%2==0):
#         even+=1
#     else:
#         odd+=1


# if(even==0):
#     print(len(num))
# else:
#     print(len(num)-1)

seta=set(a)
if(len(seta)%2==0):
    print(len(seta)-1)
else:
    print(len(seta))