s=input()
n=int(input())
for _ in range(n):
    l,r=map(int,input().split())
    s=s[:l-1]+''.join(reversed(list(s[l-1:r])))+s[r:]
#    print(s)
print(s)