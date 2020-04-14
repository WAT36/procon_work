from collections import deque
k=int(input())
cnt=0
ans=0
q=deque()
q.extend([1,2,3,4,5,6,7,8,9])

while(cnt<k):
    ans=q.popleft()
    cnt+=1
#    print(ans,cnt)
    one_digit=ans%10
    if(one_digit==0):
        q.append(int(str(ans) + '0'))
        q.append(int(str(ans) + '1'))
    elif(one_digit==9):
        q.append(int(str(ans) + '8'))
        q.append(int(str(ans) + '9'))
    else:
        q.append(int(str(ans) + str(one_digit-1)))
        q.append(int(str(ans) + str(one_digit)))
        q.append(int(str(ans) + str(one_digit+1)))
print(ans)
