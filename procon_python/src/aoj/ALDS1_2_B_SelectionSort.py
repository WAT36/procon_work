import re

def selectionSort(A):
    replacenum=0
    for i in range(len(A)):
        minj = i
        for j in range(i,len(A)):
            if(A[j] < A[minj]):
                minj = j
        if(i!=minj):
            A[i],A[minj]=A[minj],A[i]
            replacenum+=1
    return replacenum

n=int(input())
a=list(map(int,input().split()))
num=selectionSort(a)

print(re.sub("[\[\]\,]","",str(a)))
print(num)
