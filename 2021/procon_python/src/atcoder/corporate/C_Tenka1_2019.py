N = int(input())
S = list(str(input()))

right_white = S.count('.')
right_black = len(S) - right_white

ans = right_white

left_white=0
left_black=0

for i in range(N):
    if(S[i] == '#'):
        left_black = left_black+1
        right_black = right_black-1
    else:
        left_white = left_white+1
        right_white = right_white-1

    if(ans > (left_black + right_white)):
        ans = (left_black + right_white)

print(ans)