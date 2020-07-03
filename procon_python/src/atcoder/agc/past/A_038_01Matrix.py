h,w,a,b=map(int,input().split())

if(a>(w//2) and b>(h//2)):
    print('No')
else:
    for i in range(h):
        if(i<b):
            print(''.join(['0' for _ in range(a)]) + ''.join(['1' for _ in range(w-a)]))
        else:
            print(''.join(['1' for _ in range(a)]) + ''.join(['0' for _ in range(w-a)]))

