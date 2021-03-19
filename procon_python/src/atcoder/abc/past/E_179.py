n,x,m=map(int,input().split())
ai=x
ans=ai
ai_lists=[ai]
ai_set=set([])
# print(1,ai,ans)
for i in range(2,n+1):
    ai=(ai*ai)%m
    if(ai in ai_set):
        ai_cycle_start_ind=ai_lists.index(ai)
        ai_cycle_end_ind=len(ai_lists)-1
        ai_cycle_num=ai_cycle_end_ind-ai_cycle_start_ind+1
        rest_i_sum=n-(i-1)
        ans+=sum(ai_lists[ai_cycle_start_ind:])*(rest_i_sum//ai_cycle_num)

        for j in range(ai_cycle_start_ind,ai_cycle_start_ind+(rest_i_sum%ai_cycle_num)):
            ans+=ai_lists[j]
#         print(ai_lists[ai_cycle_start_ind:ai_cycle_start_ind+(rest_i_sum%ai_cycle_num)])
#         print(ai_cycle_start_ind,ai_cycle_end_ind,ai_cycle_num,rest_i_sum)
        break
    else:
        ai_lists.append(ai)
        ai_set.add(ai)
    ans+=ai
#     print(i,ai,ans,ai_lists)
print(ans)
