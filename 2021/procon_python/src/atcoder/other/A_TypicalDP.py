n=int(input())
p=list(map(int,input().split()))
all_points=[0]
for i in range(n):
    c=[all_points[j]+p[i] for j in range(len(all_points))]
    all_points = list(set(all_points + c))
print(len(all_points))