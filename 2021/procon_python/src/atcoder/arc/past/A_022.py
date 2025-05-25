s=input()
s=s.upper()
i_ind=s.find('I')
if(i_ind==-1):
    print('NO')
else:
    c_ind=s.find('C',i_ind)
    if(c_ind==-1):
        print('NO')
    else:
        t_ind=s.find('T',c_ind)
        if(t_ind==-1):
            print('NO')
        else:
            print('YES')

