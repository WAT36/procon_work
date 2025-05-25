n,a,b=map(int,input().split())
ans=(n-2)*(b-a) + 1
print(ans if ans>=0 else 0)
