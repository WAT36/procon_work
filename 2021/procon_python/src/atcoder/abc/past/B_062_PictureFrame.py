h,w=map(int,input().split())
frame=[]
frame.append("#"*(w+2))
for i in range(h):
    frame.append("#"+input()+"#")
frame.append("#"*(w+2))

for i in range(len(frame)):
    print(frame[i])