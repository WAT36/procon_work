import re
import sys
INF=10000000000000
sys.setrecursionlimit(10**6)

def merge(A,left,mid,right):
    count=0
    L=A[left:mid]
    R=A[mid:right]
    L.append(INF)
    R.append(INF)
    i=0
    j=0
    for k in range(left,right):
        if(L[i] <= R[j]):
            A[k] = L[i]
            i+=1
            count+=1
        else:
            A[k] = R[j]
            j+=1
            count+=1
    return count

def mergeSort(A,left,right):
    count=0
    if(left+1<right):
        mid=(left+right)//2
        count+=mergeSort(A, left, mid)
        count+=mergeSort(A, mid, right)
        count+=merge(A, left, mid, right)
    return count

count=0
n=int(input())
s=list(map(int,input().split()))
count=mergeSort(s, 0, n)

print(re.sub("[\[\]\,]","",str(s)))
print(count)