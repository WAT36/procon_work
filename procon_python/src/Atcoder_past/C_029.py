n=int(input())
w=["a","b","c"]
full_num=3**n
for i in range(full_num):
    temp_i = i
    temp_n = n
    password=""
    while(temp_i != 0 or temp_n != 0):
        password = w[temp_i%3] + password
        temp_i = temp_i//3
        temp_n -= 1
    print(password)