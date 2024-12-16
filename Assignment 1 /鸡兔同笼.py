a= int(input())
if a%4==0:
    max_number= int(a/2)
    min_number= int(a/4)
    print (min_number,max_number)
elif (a+2)%4==0:
    max_number= int(a/2)
    min_number= int((a+2)/4)
    print (min_number,max_number)
else:
    print(0,0)





