def binarySearch(A,key):
    left=0
    right=len(A)
    while(left < right):
        mid = (left + right)//2
        if(A[mid]==key):
            return mid
        elif(key < A[mid]):
            right = mid
        else:
            left = mid + 1
    return -1

n=int(input())
s=list(map(int,input().split()))
q=int(input())
t=list(map(int,input().split()))

ans=0
for i in range(len(t)):
    ind=binarySearch(s, t[i])
    if(ind!=-1):
        ans+=1
print(ans)
