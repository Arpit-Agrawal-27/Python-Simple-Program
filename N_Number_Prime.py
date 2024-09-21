#Program for to find the prime Number in given range
n=int(input("Enter the range of prime number:"))
if n<=1:
    print("{} is invalid input".format(n))
else:
    for num in range(2,n+1):
        res=True
        for i in range(2,num):
            if num%i==0:
                res=False
                break
        if res:
            print(num)
    else:
        print()
        print("-"*50)
