def find_narcissistic_numbers(a,b):
    result=[]
    for n in range (a,b+1):
        hundreds=n//100
        tens=n%100//10
        units=n%10

        if hundreds**3+tens**3+units**3==n:
            result.append(n)

    if result:
        print(" ".join(map(str,result)))
    else:
        print("NO")

a,b = map(int,input().split())
find_narcissistic_numbers(a,b)

