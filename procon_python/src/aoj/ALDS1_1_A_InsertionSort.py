def listShow(A):
    for i in range(len(A)):
        if(i<len(A)-1):
            print(A[i],end=' ')
        else:
            print(A[i])

def insertionSort(A,N):
    for i in range(1,N):
        j=i-1
        while(j>=0 and A[j]>A[j+1]):
            A[j],A[j+1]=A[j+1],A[j]
            j-=1
        listShow(A)

n=int(input())
a=list(map(int,input().split()))
listShow(a)
insertionSort(a,n)

