n=int(input())
num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
last=['1','0','X','9','8','7','6','5','4','3','2']
for _ in range (n):
    t=input()
    sum =0
    for i in range(17):
        sum += (ord(t[i])-48)*num[i]
    r = sum % 11
    if t[17] == last[r]:
        print ('YES')
    else:
        print('NO')
