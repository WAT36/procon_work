N,K = map(int,input().split())
d = list(map(int,input().split()))

while(True):
    n = str(N)
    flag = True
    for i in range(len(n)):
        if(int(n[i]) in d):
            flag = False
            break
    if(flag):
        break
    else:
        N += 1
print(N)
# carry = 0
# ans = ""
# for i in reversed(range(len(N))):
#     N_i = int(N[i])
#     N_i += carry
#     while(True):
#         if N_i%10 in d:
#             N_i += 1
#         else:
#             break
#     ans = str(N_i%10) + ans
#     carry = N_i//10
#
# while(carry != 0):
#     while(True):
#         if carry%10 in d:
#             carry += 1
#         else:
#             break
#     ans = str(carry%10) + ans
#     carry = carry//10
#
# print(ans)