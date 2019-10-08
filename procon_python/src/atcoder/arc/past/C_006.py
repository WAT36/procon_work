import bisect
n=int(input())
box=[1000000]
for i in range(n):
    w=int(input())
    j = bisect.bisect_left(box, w)
    if(j >= len(box)):
        box.append(w)
    else:
        box[j] = w
print(len(box))