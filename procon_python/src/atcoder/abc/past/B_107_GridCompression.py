h,w=map(int,input().split())
a=[]
allwhite_row=[]
allwhite_column=list(set([i for i in range(w)]))
for i in range(h):
    row=input()

    whitecolumn_index=row.find('.',0)
    whitecolumn=[]
    while(whitecolumn_index != -1):
        whitecolumn.append(whitecolumn_index)
        whitecolumn_index = row.find('.',whitecolumn_index+1)

    allwhite_column = list(set(allwhite_column) & set(whitecolumn))

    if(list(row).count('.')==w):
        allwhite_row.append(i)

    a.append(row)

for i in range(h):
    if(i not in allwhite_row):
        ans_i=[]
        for j in range(w):
            if(j not in allwhite_column):
                ans_i.append(a[i][j])
        print(''.join(ans_i))
