def countingSort(A,k):
    #カウント配列初期化
    C=[0 for _ in range(k+1)]

    #Aの各要素の出現数をカウント
    for i in range(len(A)):
        C[A[i]]+=1

    #カウント配列の累積和をとる->AにC[i]以下の数はいくつあるかわかる
    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]

    B=[0 for _ in range(len(A))]
    for i in range(len(A)-1,-1,-1):
#        print(i,A,B,C)
        C[A[i]]-=1
        B[C[A[i]]] = A[i]

    return B


n=int(input())
a=list(map(int,input().split()))
ans=countingSort(a, max(a))
print(*ans)
