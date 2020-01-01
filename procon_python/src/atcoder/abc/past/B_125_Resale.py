#B問題だけど解説見てやってしまった。。。
n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
diff=[v[i]-c[i] for i in range(n) if v[i]-c[i] > 0]
diff.append(0)
print(sum(diff))
