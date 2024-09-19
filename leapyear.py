a=int(input())
if (a%3200==0) or ((a%100==0) and (a%400!=0)):
    print("N")
elif a%4==0:
    print ("Y")
else:
    print("N")