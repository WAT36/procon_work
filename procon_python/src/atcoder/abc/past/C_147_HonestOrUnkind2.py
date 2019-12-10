n=int(input())
xy=[]
for i in range(n):
    ai=int(input())
    xyi=[]
    for j in range(ai):
        xyj=list(map(int,input().split()))
        xyi.append(xyj)
    xy.append(xyi)
#print(xy)

ans=0
for i in range(2**n):
    bit_i=format(i,'b').zfill(n)
    person=list(bit_i)
    clear=True
    for j in range(n):
        if(person[j]=='0'):
            continue

        xyj=xy[j]
        for k in range(len(xyj)):
            if(person[xyj[k][0]-1] != str(xyj[k][1])):
                clear=False
                break

        if(not clear):
            break

    if(clear and (ans < person.count('1'))):
#        print(person)
        ans=person.count('1')

print(ans)

# ans=0
# for i in range(2**n):
#     person=[-1 for _ in range(n)]
#     bit_i=format(i,'b').zfill(n)
#     clear=True
#     for j in range(n):
#
#         if(person[j] == -1):
#             person[j] = int(bit_i[j])
#             if(int(bit_i[j]) == 0):
#                 continue
#         elif(person[j] != int(bit_i[j])):
# #            print("{0} {1} a".format(bit_i,person))
#             clear=False
#             break
#
#         xyj=xy[j]
#         for k in range(len(xyj)):
#             if(person[xyj[k][0]-1] == -1):
#                 person[xyj[k][0]-1] = xyj[k][1]
#             elif(person[xyj[k][0]-1] != xyj[k][1]):
# #                print("{0} {1} b".format(bit_i,person))
#                 clear=False
#                 break
#
#         if(not clear):
#             break
#
#     if(clear and (ans < person.count(1))):
# #        print(bit_i)
# #        print(person)
#         ans = person.count(1)
#
# print(ans)
