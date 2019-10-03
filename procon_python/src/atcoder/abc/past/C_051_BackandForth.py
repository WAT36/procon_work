sx,sy,tx,ty = map(int,input().split())
w = abs(tx-sx)
h = abs(ty-sy)
ans = ""
ans += (("R" * w) + ("U" * h) + ("L" * w) + ("D" * h) + "D" + ("R" * (w+1)) + ("U" * (h+1)) + "LU" + ("L" * (w+1)) + ("D" * (h+1)) + "R")
print(ans)